# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import pytest

from tests import util
from tests import test_config_container
from common_test_database import invoke, networking_cleanup, networking, db_systems, db_systems_cleanup, match_on
from common_test_database import CASSETTE_LIBRARY_DIR, DB_NODE_OPERATION_TIME


@pytest.fixture(autouse=True, scope='module')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_db_node_operations.yml'):
        yield


@pytest.fixture(scope='module')
def networking_test_db_node_operations(runner, config_file, config_profile, network_client, request):
    subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client, "_db_node_operations")
    yield networking_dict
    networking_cleanup(runner, config_file, config_profile, network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


@pytest.fixture(scope='module')
def db_systems_test_db_node_operations(runner, config_file, config_profile, networking_test_db_node_operations, network_client, request):
    db_system_id_1, db_system_id_2 = db_systems(runner, config_file, config_profile, networking_test_db_node_operations, network_client, request)
    yield [db_system_id_1, db_system_id_2]
    db_systems_cleanup(runner, config_file, config_profile, db_system_id_1, db_system_id_2)


@util.long_running
def test_db_node_operations(runner, config_file, config_profile, db_systems_test_db_node_operations):
    # list nodes in db-system
    params = [
        'node', 'list',
        '--compartment-id', util.COMPARTMENT_ID,
        '--db-system-id', db_systems_test_db_node_operations[0]
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    json_result = json.loads(result.output)

    # assert there is at least one node in the system
    assert len(json_result['data']) > 0

    node_id = json_result['data'][0]['id']

    # get node
    params = [
        'node', 'get',
        '--db-node-id', node_id
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    #
    # test node actions
    #

    # db node stop
    params = [
        'node', 'stop',
        '--db-node-id', node_id
    ]
    print('Stopping DB Node...')
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert json.loads(result.output)['data']['lifecycle-state'] == "STOPPING"

    # db node start
    params = [
        'node', 'start',
        '--db-node-id', node_id
    ]
    print('Starting DB Node...')
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert json.loads(result.output)['data']['lifecycle-state'] == "STARTING"

    # db node reset
    params = [
        'node', 'reset',
        '--db-node-id', node_id
    ]
    print('Reseting DB Node...')
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert json.loads(result.output)['data']['lifecycle-state'] == "STOPPING"

    params = [
        'node', 'get',
        '--db-node-id', node_id
    ]
    result = invoke(runner, config_file, config_profile, params)
    reset_state = json.loads(result.output)['data']['lifecycle-state']
    while reset_state == "STOPPING" or reset_state == "STOPPED":
        result = invoke(runner, config_file, config_profile, params)
        reset_state = json.loads(result.output)['data']['lifecycle-state']
        print(result.output)

    # db node soft-reset
    params = [
        'node', 'soft-reset',
        '--db-node-id', node_id
    ]
    print('Soft reseting DB Node...')
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert json.loads(result.output)['data']['lifecycle-state'] == "STOPPING"
    util.wait_until(['db', 'system', 'get', '--db-system-id', db_systems_test_db_node_operations[0]], 'AVAILABLE', max_wait_seconds=DB_NODE_OPERATION_TIME)
