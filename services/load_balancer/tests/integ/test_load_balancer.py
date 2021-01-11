# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import oci_cli
import os
import pytest
from tests import tag_data_container
from tests import test_config_container
from tests import util

LB_PROVISIONING_TIME_SEC = 300  # 5 minutes
LB_PRIVATE_KEY_PASSPHRASE = 'secret!'

DEFAULT_WAIT_TIME = 120  # 1 minute
CASSETTE_LIBRARY_DIR = 'services/load_balancer/tests/cassettes'
TEMP_DIR = os.path.join('tests', 'temp')


@pytest.fixture(scope='module')
def load_balancer(runner, config_file, config_profile, vcn_and_subnets):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_fixture_lb.yml'):
        subnet_ocid_1 = vcn_and_subnets[1]
        subnet_ocid_2 = vcn_and_subnets[2]

        params = [
            'load-balancer', 'create',
            '-c', util.COMPARTMENT_ID,
            '--display-name', util.random_name('cli_lb'),
            '--shape-name', '100Mbps',
            '--subnet-ids', '["{}","{}"]'.format(subnet_ocid_1, subnet_ocid_2)
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # create lb returns work request
        response = json.loads(result.output)
        work_request_ocid = response['opc-work-request-id']

        get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=LB_PROVISIONING_TIME_SEC)
        util.validate_response(get_work_request_result)

        lb_ocid = json.loads(get_work_request_result.output)['data']['load-balancer-id']

        yield lb_ocid

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_fixture_lb_delete.yml'):
        params = [
            'load-balancer', 'delete',
            '--load-balancer-id', lb_ocid,
            '--force'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        util.wait_until(['lb', 'load-balancer', 'get', '--load-balancer-id', lb_ocid], 'TERMINATED', max_wait_seconds=LB_PROVISIONING_TIME_SEC, succeed_if_not_found=True)


@pytest.fixture(scope='module')
def backend_set(runner, config_file, config_profile, load_balancer):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_fixture_backend_set.yml'):
        backend_set_name = util.random_name('cli_lb_backend_set')

        params = [
            'backend-set', 'create',
            '--name', backend_set_name,
            '--policy', 'ROUND_ROBIN',
            '--load-balancer-id', load_balancer,
            '--health-checker-protocol', 'HTTP',
            '--health-checker-return-code', '200',
            '--health-checker-url-path', '/healthcheck',
            '--health-checker-interval-in-ms', '60000',  # 1 minute
            '--session-persistence-cookie-name', '*',
            '--session-persistence-disable-fallback', 'false'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # create lb returns work request
        response = json.loads(result.output)
        work_request_ocid = response['opc-work-request-id']

        get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=DEFAULT_WAIT_TIME)
        util.validate_response(get_work_request_result)

        yield backend_set_name

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_fixture_backend_set_delete.yml'):
        params = [
            'backend-set', 'delete',
            '--load-balancer-id', load_balancer,
            '--backend-set-name', backend_set_name,
            '--force'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        response = json.loads(result.output)
        work_request_ocid = response['opc-work-request-id']

        get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=DEFAULT_WAIT_TIME)
        util.validate_response(get_work_request_result)


@pytest.fixture(scope='module')
def backend(runner, config_file, config_profile, load_balancer, backend_set):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_fixture_backend.yml'):
        ip_address = '10.0.0.10'
        port = '80'
        params = [
            'backend', 'create',
            '--ip-address', ip_address,
            '--port', port,
            '--load-balancer-id', load_balancer,
            '--backend-set-name', backend_set,
            '--weight', '3'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # returns work request
        response = json.loads(result.output)
        work_request_ocid = response['opc-work-request-id']

        get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=DEFAULT_WAIT_TIME)
        util.validate_response(get_work_request_result)

        # backend name defaults to "ipaddress:port"
        backend_name = "{}:{}".format(ip_address, port)
        yield backend_name

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_fixture_backend_delete.yml'):
        params = [
            'backend', 'delete',
            '--load-balancer-id', load_balancer,
            '--backend-set-name', backend_set,
            '--backend-name', backend_name,
            '--force'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # returns work request
        response = json.loads(result.output)
        work_request_ocid = response['opc-work-request-id']

        get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=DEFAULT_WAIT_TIME)
        util.validate_response(get_work_request_result)


@pytest.fixture(scope='module')
def certificate(runner, config_file, config_profile, load_balancer, key_pair_files):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_fixture_certificate.yml'):
        private_key_filename = key_pair_files[1]
        certificate_filename = key_pair_files[2]

        cert_name = util.random_name('cli_lb_certificate')

        params = [
            'certificate', 'create',
            '--certificate-name', cert_name,
            '--load-balancer-id', load_balancer,
            '--ca-certificate-file', certificate_filename,
            '--private-key-file', private_key_filename,
            '--public-certificate-file', certificate_filename,
            '--passphrase', LB_PRIVATE_KEY_PASSPHRASE
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # returns work request
        response = json.loads(result.output)
        work_request_ocid = response['opc-work-request-id']

        get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=LB_PROVISIONING_TIME_SEC)
        util.validate_response(get_work_request_result)

        yield cert_name

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_fixture_certificate_delete.yml'):
        # delete cert
        params = [
            'certificate', 'delete',
            '--load-balancer-id', load_balancer,
            '--certificate-name', cert_name,
            '--force'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        response = json.loads(result.output)
        work_request_ocid = response['opc-work-request-id']

        get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=LB_PROVISIONING_TIME_SEC)
        util.validate_response(get_work_request_result)


@util.slow
def test_load_balancer_operations(runner, config_file, config_profile, load_balancer):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_lb_operations.yml'):
        # list
        params = [
            'load-balancer', 'list',
            '-c', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        load_balancers = json.loads(result.output)['data']

        found_lb = False
        for lb in load_balancers:
            if lb['id'] == load_balancer:
                found_lb = True

        assert found_lb

        # update
        # params = [
        #     'load-balancer', 'update',
        #     '--load-balancer-id', load_balancer,
        #     '--display-name', util.random_name('cli_lb_updated')
        # ]

        # result = invoke(runner, config_file, config_profile, params)
        # util.validate_response(result)

        # # returns work request
        # response = json.loads(result.output)
        # work_request_ocid = response['opc-work-request-id']

        # get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=DEFAULT_WAIT_TIME)
        # util.validate_response(get_work_request_result)

        # get
        params = [
            'load-balancer', 'get',
            '--load-balancer-id', load_balancer
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # assert 'cli_lb_updated' in json.loads(result.output)['data']['display-name']


@util.slow
def test_certificate_operations(runner, config_file, config_profile, load_balancer, certificate):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_cert_operations.yml'):
        params = [
            'certificate', 'list',
            '--load-balancer-id', load_balancer
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        response = json.loads(result.output)
        found_cert = False
        for cert in response['data']:
            if cert['certificate-name'] == certificate:
                found_cert = True

        assert found_cert


@util.slow
def test_backend_set_operations(runner, config_file, config_profile, load_balancer, backend_set):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_backend_set_operations.yml'):
        # fixture handles create / delete
        params = [
            'backend-set', 'list',
            '--load-balancer-id', load_balancer
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        params = [
            'backend-set', 'get',
            '--load-balancer-id', load_balancer,
            '--backend-set-name', backend_set
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        params = [
            'backend-set', 'update',
            '--load-balancer-id', load_balancer,
            '--backend-set-name', backend_set,
            '--backends', '[]',
            '--policy', 'ROUND_ROBIN',
            '--health-checker-protocol', 'HTTP',
            '--health-checker-url-path', '/healthchecker',
            '--force'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # returns work request
        response = json.loads(result.output)
        work_request_ocid = response['opc-work-request-id']

        get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=DEFAULT_WAIT_TIME)
        util.validate_response(get_work_request_result)


@util.slow
def test_backend_operations(runner, config_file, config_profile, load_balancer, backend_set, backend):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_backend_operations.yml'):
        # fixture handles create / delete
        params = [
            'backend', 'list',
            '--load-balancer-id', load_balancer,
            '--backend-set-name', backend_set
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        params = [
            'backend', 'update',
            '--load-balancer-id', load_balancer,
            '--backend-set-name', backend_set,
            '--backend-name', backend,
            '--weight', '2',
            '--offline', 'true',
            '--backup', 'false',
            '--drain', 'false'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # returns work request
        response = json.loads(result.output)
        work_request_ocid = response['opc-work-request-id']

        get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=DEFAULT_WAIT_TIME)
        util.validate_response(get_work_request_result)


@util.slow
def test_listener_operations(runner, config_file, config_profile, load_balancer, backend_set, certificate):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_listener_operations.yml'):
        # create listener
        listener_name = util.random_name('cli_listener')
        params = [
            'listener', 'create',
            '--default-backend-set-name', backend_set,
            '--load-balancer-id', load_balancer,
            '--name', listener_name,
            '--port', '8080',
            '--protocol', 'HTTP',
            '--ssl-certificate-name', certificate
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # returns a work request
        response = json.loads(result.output)
        work_request_ocid = response['opc-work-request-id']

        get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=LB_PROVISIONING_TIME_SEC)
        util.validate_response(get_work_request_result)

        # update listener
        params = [
            'listener', 'update',
            '--listener-name', listener_name,
            '--default-backend-set-name', backend_set,
            '--load-balancer-id', load_balancer,
            '--port', '8080',
            '--protocol', 'HTTP',
            '--ssl-certificate-name', certificate,
            '--force'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # returns a work request
        response = json.loads(result.output)
        work_request_ocid = response['opc-work-request-id']

        get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=LB_PROVISIONING_TIME_SEC)
        util.validate_response(get_work_request_result)

        # delete listener
        params = [
            'listener', 'delete',
            '--load-balancer-id', load_balancer,
            '--listener-name', listener_name,
            '--force'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # returns a work request
        response = json.loads(result.output)
        work_request_ocid = response['opc-work-request-id']

        get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=LB_PROVISIONING_TIME_SEC)
        util.validate_response(get_work_request_result)


@util.slow
def test_listener_with_connection_timeout_operations(runner, config_file, config_profile, load_balancer, backend_set):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_listener_with_connection_timeout_operations.yml'):
        listener_name = util.random_name('cli_listener_ct')
        params = [
            'listener', 'create',
            '--default-backend-set-name', backend_set,
            '--load-balancer-id', load_balancer,
            '--name', listener_name,
            '--port', '8080',
            '--protocol', 'HTTP',
            '--connection-configuration-idle-timeout', '100',
            '--wait-for-state', 'SUCCEEDED'
        ]
        result = invoke(runner, config_file, config_profile, params)
        _validate_work_request_result(result, load_balancer)

        result = invoke(runner, config_file, config_profile, ['load-balancer', 'get', '--load-balancer-id', load_balancer])
        parsed_result = json.loads(result.output)
        assert parsed_result['data']['listeners'][listener_name]['connection-configuration']['idle-timeout'] == 100

        params = [
            'listener', 'update',
            '--listener-name', listener_name,
            '--default-backend-set-name', backend_set,
            '--load-balancer-id', load_balancer,
            '--port', '8080',
            '--protocol', 'HTTP',
            '--connection-configuration-idle-timeout', '75',
            '--force',
            '--wait-for-state', 'SUCCEEDED'
        ]
        result = invoke(runner, config_file, config_profile, params)
        _validate_work_request_result(result, load_balancer)

        result = invoke(runner, config_file, config_profile, ['load-balancer', 'get', '--load-balancer-id', load_balancer])
        parsed_result = json.loads(result.output)
        assert parsed_result['data']['listeners'][listener_name]['connection-configuration']['idle-timeout'] == 75

        params = [
            'listener', 'delete',
            '--load-balancer-id', load_balancer,
            '--listener-name', listener_name,
            '--force',
            '--wait-for-state', 'SUCCEEDED'
        ]
        result = invoke(runner, config_file, config_profile, params)
        _validate_work_request_result(result, load_balancer)


@util.slow
def test_load_balancer_health_operations(runner, config_file, config_profile, load_balancer):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_lb_health_operations.yml'):
        params = [
            'load-balancer-health', 'get',
            '--load-balancer-id', load_balancer
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        params = [
            'load-balancer-health', 'list',
            '-c', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


@util.slow
def test_backend_set_health_operations(runner, config_file, config_profile, load_balancer, backend_set):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_backend_set_health_operations.yml'):
        params = [
            'backend-set-health', 'get',
            '--load-balancer-id', load_balancer,
            '--backend-set-name', backend_set
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


@util.slow
def test_backend_health_operations(runner, config_file, config_profile, load_balancer, backend_set, backend):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_backend_health_operations.yml'):
        params = [
            'backend-health', 'get',
            '--load-balancer-id', load_balancer,
            '--backend-set-name', backend_set,
            '--backend-name', backend
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


@util.slow
def test_health_checker_operations(runner, config_file, config_profile, load_balancer, backend_set):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_health_checker_operations.yml'):
        params = [
            'health-checker', 'update',
            '--load-balancer-id', load_balancer,
            '--backend-set-name', backend_set,
            '--interval-in-millis', '15000',
            '--port', '80',
            '--protocol', 'HTTP',
            '--response-body-regex', '.*',
            '--retries', '3',
            '--return-code', '200',
            '--timeout-in-millis', '1000',
            '--url-path', '/healthcheck'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # health-checker update returns work request
        response = json.loads(result.output)
        work_request_ocid = response['opc-work-request-id']

        get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=LB_PROVISIONING_TIME_SEC)
        util.validate_response(get_work_request_result)

        params = [
            'health-checker', 'get',
            '--load-balancer-id', load_balancer,
            '--backend-set-name', backend_set
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        assert 15000 == json.loads(result.output)['data']['interval-in-millis']


def test_list_lb_shapes(runner, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_lb_shapes.yml'):
        params = [
            'shape', 'list',
            '-c', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


def test_list_lb_protocols(runner, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_lb_protocols.yml'):
        params = [
            'protocol', 'list',
            '-c', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


def test_list_lb_policy(runner, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_lb_policy.yml'):
        params = [
            'policy', 'list',
            '-c', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


def test_load_balancer_operations_with_waiters(runner, config_file, config_profile, vcn_and_subnets, key_pair_files):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_ops_with_waiters.yml'):
        subnet_ocid_1 = vcn_and_subnets[1]
        subnet_ocid_2 = vcn_and_subnets[2]

        lb_name = util.random_name('cli_lb')
        params = [
            'load-balancer', 'create',
            '-c', util.COMPARTMENT_ID,
            '--display-name', lb_name,
            '--shape-name', '100Mbps',
            '--subnet-ids', '["{}","{}"]'.format(subnet_ocid_1, subnet_ocid_2),
            '--wait-for-state', 'SUCCEEDED'
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result, json_response_expected=False)
        load_balancer = util.get_json_from_mixed_string(result.output)
        assert load_balancer['data']['lifecycle-state'] == 'ACTIVE'
        assert 'loadbalancer' in load_balancer['data']['id']
        assert load_balancer['data']['display-name'] == lb_name
        assert load_balancer['data']['shape-name'] == '100Mbps'
        assert len(load_balancer['data']['subnet-ids']) == 2
        assert subnet_ocid_1 in load_balancer['data']['subnet-ids']
        assert subnet_ocid_2 in load_balancer['data']['subnet-ids']

        _do_backend_and_backend_set_waiters(runner, load_balancer['data']['id'], config_file, config_profile)
        _do_certificate_waiters(runner, load_balancer['data']['id'], config_file, config_profile, key_pair_files)

        params = [
            'load-balancer', 'delete',
            '--load-balancer-id', load_balancer['data']['id'],
            '--force',
            '--wait-for-state', 'SUCCEEDED'
        ]
        result = invoke(runner, config_file, config_profile, params)
        _validate_work_request_result(result, load_balancer['data']['id'])


@pytest.mark.usefixtures("tag_namespace_and_tags")
def test_load_balancer_tagging(runner, config_file, config_profile, vcn_and_subnets, key_pair_files):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_load_balancer_tagging.yml'):
        subnet_ocid_1 = vcn_and_subnets[1]
        subnet_ocid_2 = vcn_and_subnets[2]

        # Setup the tag inputs
        tag_names_to_values = {}
        for t in tag_data_container.tags:
            tag_names_to_values[t.name] = 'somevalue {}'.format(t.name)
        tag_data_container.write_defined_tags_to_file(
            os.path.join('tests', 'temp', 'defined_tags_lb.json'),
            tag_data_container.tag_namespace,
            tag_names_to_values
        )

        # Create the LB with tags
        lb_name = util.random_name('cli_lb')
        params = [
            'load-balancer', 'create',
            '-c', util.COMPARTMENT_ID,
            '--display-name', lb_name,
            '--shape-name', '100Mbps',
            '--subnet-ids', '["{}","{}"]'.format(subnet_ocid_1, subnet_ocid_2),
            '--freeform-tags', 'file://tests/resources/tagging/freeform_tags_2.json',
            '--defined-tags', 'file://tests/temp/defined_tags_lb.json',
            '--wait-for-state', 'SUCCEEDED',
            '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result, json_response_expected=False)
        load_balancer = util.get_json_from_mixed_string(result.output)
        id = load_balancer['data']['id']

        try:
            # Make sure the tags are in the results
            assert "tagOne" in load_balancer['data']['freeform-tags']
            assert "value three" == load_balancer['data']['freeform-tags']["tagOne"]
            assert "cli_tag_ns_320683" in load_balancer['data']['defined-tags']
            assert "cli_tag_320683" in load_balancer['data']['defined-tags']['cli_tag_ns_320683']
            assert "cli_tag_320683" in load_balancer['data']['defined-tags']['cli_tag_ns_320683']
            assert "somevalue cli_tag_320683" == load_balancer['data']['defined-tags']['cli_tag_ns_320683']['cli_tag_320683']

            # Get the LB and make sure the tags are in the results
            params = [
                'load-balancer', 'get',
                '--load-balancer-id', id
            ]
            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result, json_response_expected=False)
            load_balancer = util.get_json_from_mixed_string(result.output)
            id = load_balancer['data']['id']
            assert "tagOne" in load_balancer['data']['freeform-tags']
            assert "value three" == load_balancer['data']['freeform-tags']["tagOne"]
            assert "cli_tag_ns_320683" in load_balancer['data']['defined-tags']
            assert "cli_tag_320683" in load_balancer['data']['defined-tags']['cli_tag_ns_320683']
            assert "cli_tag_320683" in load_balancer['data']['defined-tags']['cli_tag_ns_320683']
            assert "somevalue cli_tag_320683" == load_balancer['data']['defined-tags']['cli_tag_ns_320683']['cli_tag_320683']

            # List the LB and check that the tags are in the result
            params = [
                'load-balancer', 'list',
                '-c', util.COMPARTMENT_ID
            ]
            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result, json_response_expected=False)
            list_result = util.get_json_from_mixed_string(result.output)
            if len(list_result['data']) == 1:
                load_balancer = list_result['data'][0]
                assert "tagOne" in load_balancer['freeform-tags']
                assert "value three" == load_balancer['freeform-tags']["tagOne"]
                assert "cli_tag_ns_320683" in load_balancer['defined-tags']
                assert "cli_tag_320683" in load_balancer['defined-tags']['cli_tag_ns_320683']
                assert "cli_tag_320683" in load_balancer['defined-tags']['cli_tag_ns_320683']
                assert "somevalue cli_tag_320683" == load_balancer['defined-tags']['cli_tag_ns_320683']['cli_tag_320683']

            # Update the display name for the lb.
            params = [
                'load-balancer', 'update',
                '--load-balancer-id', id,
                '--display-name', 'new' + lb_name,
                '--wait-for-state', 'SUCCEEDED'
            ]
            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result, json_response_expected=False)

            params = [
                'load-balancer', 'get',
                '--load-balancer-id', id
            ]
            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result, json_response_expected=False)
            load_balancer = util.get_json_from_mixed_string(result.output)
            assert "new" + lb_name == load_balancer['data']['display-name']

            # Setup the tag inputs
            tag_names_to_values = {}
            for t in tag_data_container.tags:
                tag_names_to_values[t.name] = 'newvalue {}'.format(t.name)
            tag_data_container.write_defined_tags_to_file(
                os.path.join('tests', 'temp', 'defined_tags_lb.json'),
                tag_data_container.tag_namespace,
                tag_names_to_values
            )

            # Update the tags for the lb.
            params = [
                'load-balancer', 'update',
                '--load-balancer-id', id,
                '--freeform-tags', 'file://tests/resources/tagging/freeform_tags_1.json',
                '--defined-tags', 'file://tests/temp/defined_tags_lb.json',
                '--wait-for-state', 'SUCCEEDED',
                '--force'
            ]
            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result, json_response_expected=False)

            params = [
                'load-balancer', 'get',
                '--load-balancer-id', id
            ]
            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result, json_response_expected=False)
            load_balancer = util.get_json_from_mixed_string(result.output)
            assert "tagOne" in load_balancer['data']['freeform-tags']
            assert "tag_Two" in load_balancer['data']['freeform-tags']
            assert "value1" == load_balancer['data']['freeform-tags']["tagOne"]
            assert "value two" == load_balancer['data']['freeform-tags']["tag_Two"]
            assert "cli_tag_ns_320683" in load_balancer['data']['defined-tags']
            assert "cli_tag_320683" in load_balancer['data']['defined-tags']['cli_tag_ns_320683']
            assert "newvalue cli_tag_320683" == load_balancer['data']['defined-tags']['cli_tag_ns_320683']['cli_tag_320683']

        finally:
            # Delete the LB
            params = [
                'load-balancer', 'delete',
                '--load-balancer-id', id,
                '--force',
                '--wait-for-state', 'SUCCEEDED',
                '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS
            ]
            result = invoke(runner, config_file, config_profile, params)
            _validate_work_request_result(result, id)


def _do_backend_and_backend_set_waiters(runner, load_balancer_id, config_file, config_profile):
    backend_set_name = util.random_name('cli_lb_backend_set')

    params = [
        'backend-set', 'create',
        '--name', backend_set_name,
        '--policy', 'ROUND_ROBIN',
        '--load-balancer-id', load_balancer_id,
        '--health-checker-protocol', 'HTTP',
        '--health-checker-return-code', '200',
        '--health-checker-url-path', '/healthcheck',
        '--health-checker-interval-in-ms', '60000',  # 1 minute
        '--session-persistence-cookie-name', '*',
        '--session-persistence-disable-fallback', 'false',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)

    ip_address = '10.0.0.10'
    port = '80'
    params = [
        'backend', 'create',
        '--ip-address', ip_address,
        '--port', port,
        '--load-balancer-id', load_balancer_id,
        '--backend-set-name', backend_set_name,
        '--weight', '3',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)

    backend_name = "{}:{}".format(ip_address, port)
    params = [
        'backend', 'update',
        '--load-balancer-id', load_balancer_id,
        '--backend-set-name', backend_set_name,
        '--backend-name', backend_name,
        '--weight', '2',
        '--offline', 'true',
        '--backup', 'false',
        '--drain', 'false',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)

    params = [
        'backend', 'delete',
        '--load-balancer-id', load_balancer_id,
        '--backend-set-name', backend_set_name,
        '--backend-name', backend_name,
        '--force',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)

    _do_listener_waiters(runner, load_balancer_id, backend_set_name, config_file, config_profile)

    params = [
        'backend-set', 'delete',
        '--load-balancer-id', load_balancer_id,
        '--backend-set-name', backend_set_name,
        '--force',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)


def _do_certificate_waiters(runner, load_balancer_id, config_file, config_profile, key_pair_files):
    private_key_filename = key_pair_files[1]
    certificate_filename = key_pair_files[2]

    cert_name = util.random_name('cli_lb_certificate')

    params = [
        'certificate', 'create',
        '--certificate-name', cert_name,
        '--load-balancer-id', load_balancer_id,
        '--ca-certificate-file', certificate_filename,
        '--private-key-file', private_key_filename,
        '--public-certificate-file', certificate_filename,
        '--passphrase', 'secret!',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)

    params = [
        'certificate', 'delete',
        '--load-balancer-id', load_balancer_id,
        '--certificate-name', cert_name,
        '--force',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)


def _do_listener_waiters(runner, load_balancer_id, backend_set_name, config_file, config_profile):
    listener_name = util.random_name('cli_listener')
    params = [
        'listener', 'create',
        '--default-backend-set-name', backend_set_name,
        '--load-balancer-id', load_balancer_id,
        '--name', listener_name,
        '--port', '8080',
        '--protocol', 'HTTP',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)

    params = [
        'listener', 'update',
        '--listener-name', listener_name,
        '--default-backend-set-name', backend_set_name,
        '--load-balancer-id', load_balancer_id,
        '--port', '8080',
        '--protocol', 'HTTP',
        '--force',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)

    params = [
        'listener', 'delete',
        '--load-balancer-id', load_balancer_id,
        '--listener-name', listener_name,
        '--force',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)


def _validate_work_request_result(result, load_balancer_id):
    util.validate_response(result, json_response_expected=False)
    assert 'Action completed. Waiting until the work request has entered state:' in result.output

    work_request = util.get_json_from_mixed_string(result.output)
    assert work_request['data']['load-balancer-id'] == load_balancer_id
    assert work_request['data']['lifecycle-state'] == 'SUCCEEDED'


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile', config_profile, 'lb'] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + ['--config-file', config_file, '--profile', config_profile, 'lb'] + params, ** args)

    return result
