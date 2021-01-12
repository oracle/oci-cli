# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import pytest

from tests import util
from tests import test_config_container
from common_test_database import invoke, networking_cleanup, networking, db_systems, db_systems_cleanup, get_database, match_on
from common_test_database import CASSETTE_LIBRARY_DIR, ADMIN_PASSWORD, DATA_GUARD_ASSOCIATION_OPERATION_TIME


@pytest.fixture(autouse=True, scope='module')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_data_guard_operations.yml'):
        yield


@pytest.fixture(scope='module')
def networking_test_data_guard_operations(runner, config_file, config_profile, network_client, request):
    subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client, "_test_data_guard_operations")
    yield networking_dict
    networking_cleanup(runner, config_file, config_profile, network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


@pytest.fixture(scope='module')
def db_systems_test_data_guard_operations(runner, config_file, config_profile, networking_test_data_guard_operations, network_client, request):
    db_system_id_1, db_system_id_2 = db_systems(runner, config_file, config_profile, networking_test_data_guard_operations, network_client, request)
    yield [db_system_id_1, db_system_id_2]
    db_systems_cleanup(runner, config_file, config_profile, db_system_id_1, db_system_id_2)


@pytest.fixture(scope='module')
def database_test_data_guard_operations(runner, config_file, config_profile, db_systems_test_data_guard_operations):
    return get_database(runner, config_file, config_profile, db_systems_test_data_guard_operations)


@util.long_running
def test_data_guard_operations(runner, config_file, config_profile, database_test_data_guard_operations, db_systems_test_data_guard_operations):
    # verify db system 1 is available
    params = [
        'system', 'get',
        '--db-system-id', db_systems_test_data_guard_operations[0]
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    db_system_1_state = json.loads(result.output)['data']['lifecycle-state']

    # verify db system 2 is available
    params = [
        'system', 'get',
        '--db-system-id', db_systems_test_data_guard_operations[1]
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    db_system_2_state = json.loads(result.output)['data']['lifecycle-state']

    if db_system_1_state != "AVAILABLE":
        print("Waiting for DB system 1 to become AVAILABLE")
        util.wait_until(['db', 'system', 'get', '--db-system-id', db_systems_test_data_guard_operations[0]], 'AVAILABLE', max_wait_seconds=300)

    if db_system_2_state != "AVAILABLE":
        print("Waiting for DB system 2 to become AVAILABLE")
        util.wait_until(['db', 'system', 'get', '--db-system-id', db_systems_test_data_guard_operations[1]], 'AVAILABLE', max_wait_seconds=300)

    # CREATE
    # data guard requires 2 distinct DB systems
    # 'database' comes from db_systems[0] and db_systems[1] is used as the peer db system
    print("Creating Data Guard Association. . .")
    params = [
        'data-guard-association', 'create', 'from-existing-db-system',
        '--database-id', database_test_data_guard_operations,
        '--creation-type', 'ExistingDbSystem',
        '--database-admin-password', ADMIN_PASSWORD,
        '--protection-mode', 'MAXIMUM_PERFORMANCE',
        '--transport-type', 'ASYNC',
        '--peer-db-system-id', db_systems_test_data_guard_operations[1]
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    data_guard_association_id = json.loads(result.output)['data']['id']

    util.wait_until(['db', 'data-guard-association', 'get', '--database-id', database_test_data_guard_operations, '--data-guard-association-id', data_guard_association_id], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)

    util.wait_until(['db', 'system', 'get', '--db-system-id', db_systems_test_data_guard_operations[0]], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
    util.wait_until(['db', 'system', 'get', '--db-system-id', db_systems_test_data_guard_operations[1]], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)

    # LIST
    params = [
        'data-guard-association', 'list',
        '--database-id', database_test_data_guard_operations
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    assert len(json.loads(result.output)['data']) > 0

    # GET
    params = [
        'data-guard-association', 'get',
        '--database-id', database_test_data_guard_operations,
        '--data-guard-association-id', data_guard_association_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    peer_database_id = json.loads(result.output)['data']['peer-database-id']
    peer_data_guard_association_id = json.loads(result.output)['data']['peer-data-guard-association-id']

    # ensure both databases are available
    util.wait_until(['db', 'database', 'get', '--database-id', database_test_data_guard_operations], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
    util.wait_until(['db', 'database', 'get', '--database-id', peer_database_id], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)

    # FAILOVER
    # Data Guard Association action FAILOVER only allowed on Standby database.
    #   - Primary -> disabled_standby
    #   - Standby -> Primary
    print("Attempting Data Guard failover...")
    params = [
        'data-guard-association', 'failover',
        '--database-id', peer_database_id,
        '--data-guard-association-id', peer_data_guard_association_id,
        '--database-admin-password', ADMIN_PASSWORD
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # wait until both databases are available again
    util.wait_until(['db', 'database', 'get', '--database-id', database_test_data_guard_operations], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
    util.wait_until(['db', 'database', 'get', '--database-id', peer_database_id], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)

    # REINSTATE
    # 'disabled_standby' -> standby
    print("Attempting Data Guard reinstate...")
    params = [
        'data-guard-association', 'reinstate',
        '--database-id', peer_database_id,
        '--data-guard-association-id', peer_data_guard_association_id,
        '--database-admin-password', ADMIN_PASSWORD
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    util.wait_until(['db', 'database', 'get', '--database-id', database_test_data_guard_operations], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
    util.wait_until(['db', 'database', 'get', '--database-id', peer_database_id], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)

    # SWITCHOVER
    # primary (original standby) -> standby
    # standby (original primary) -> primary
    print("Attempting Data Guard switchover...")
    params = [
        'data-guard-association', 'switchover',
        '--database-id', peer_database_id,
        '--data-guard-association-id', peer_data_guard_association_id,
        '--database-admin-password', ADMIN_PASSWORD
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    util.wait_until(['db', 'database', 'get', '--database-id', database_test_data_guard_operations], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
    util.wait_until(['db', 'database', 'get', '--database-id', peer_database_id], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)

    # DELETE DATA GUARD ASSOCIATION BY DELETING STANDBY DB (this allows us to clean up the DB System)
    print("Deleting peer database...")
    params = [
        'database', 'delete',
        '--database-id', peer_database_id,
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    util.wait_until(['db', 'database', 'get', '--database-id', peer_database_id], 'TERMINATED', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME, succeed_if_not_found=True)
