# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import pytest

from tests import util
from tests import test_config_container
from common_test_database import invoke, networking_cleanup, networking, get_database, vm_db_system, vm_db_system_cleanup, match_on
from common_test_database import CASSETTE_LIBRARY_DIR, ADMIN_PASSWORD, DB_SYSTEM_PROVISIONING_TIME_SEC, DATA_GUARD_ASSOCIATION_OPERATION_TIME


@pytest.fixture(autouse=True, scope='module')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_data_guard_with_new_db.yml'):
        yield


@pytest.fixture(scope='module')
def networking_test_data_guard_with_new_db(runner, config_file, config_profile, network_client, request):
    subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client, "_data_guard_with_new_db")
    yield networking_dict
    networking_cleanup(runner, config_file, config_profile, network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


@pytest.fixture(scope='module')
def vm_db_system_test_data_guard_with_new_db(runner, config_file, config_profile, networking_test_data_guard_with_new_db, network_client, request):
    db_system_id_1 = vm_db_system(runner, config_file, config_profile, networking_test_data_guard_with_new_db, network_client, request)
    yield [db_system_id_1, ]
    vm_db_system_cleanup(runner, config_file, config_profile, db_system_id_1)


@pytest.fixture(scope='module')
def vm_database_test_data_guard_with_new_db(runner, config_file, config_profile, vm_db_system_test_data_guard_with_new_db):
    return get_database(runner, config_file, config_profile, vm_db_system_test_data_guard_with_new_db)


@util.long_running
def test_data_guard_with_new_db(runner, config_file, config_profile, vm_database_test_data_guard_with_new_db, vm_db_system_test_data_guard_with_new_db):
    # Get the subnet of the existing database
    params = ['system', 'get', '--db-system-id', vm_db_system_test_data_guard_with_new_db[0]]
    result = invoke(runner, config_file, config_profile, params)
    subnet_id = json.loads(result.output)['data']['subnet-id']
    availability_domain = json.loads(result.output)['data']['availability-domain']

    # CREATE using a new DB rather than an existing one.
    # 'database' comes from vm_db_system_test_data_guard_with_new_db[0] and the second one will be created.
    print("Creating Data Guard Association...")
    params = [
        'data-guard-association', 'create', 'with-new-db-system',
        '--database-id', vm_database_test_data_guard_with_new_db,
        '--creation-type', 'NewDbSystem',
        '--database-admin-password', ADMIN_PASSWORD,
        '--protection-mode', 'MAXIMUM_PERFORMANCE',
        '--transport-type', 'ASYNC',
        '--availability-domain', availability_domain,
        '--display-name', 'DataGuardDb',
        # The combined hostname and domain cannot be longer than 56 characters.
        '--hostname', 'host-dg-new-db',
        '--subnet-id', subnet_id
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    data_guard_association_id = json.loads(result.output)['data']['id']
    print("data-guard-association", result.output)
    util.wait_until(['db', 'data-guard-association', 'get', '--database-id', vm_database_test_data_guard_with_new_db, '--data-guard-association-id', data_guard_association_id], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
    util.wait_until(['db', 'system', 'get', '--db-system-id', vm_db_system_test_data_guard_with_new_db[0]], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)

    # LIST
    params = [
        'data-guard-association', 'list',
        '--database-id', vm_database_test_data_guard_with_new_db
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert len(json.loads(result.output)['data']) > 0

    # GET
    params = [
        'data-guard-association', 'get',
        '--database-id', vm_database_test_data_guard_with_new_db,
        '--data-guard-association-id', data_guard_association_id
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    peer_database_id = json.loads(result.output)['data']['peer-database-id']
    peer_db_system_id = json.loads(result.output)['data']['peer-db-system-id']
    peer_data_guard_association_id = json.loads(result.output)['data']['peer-data-guard-association-id']
    # ensure both databases are available
    util.wait_until(['db', 'database', 'get', '--database-id', vm_database_test_data_guard_with_new_db], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
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
    util.wait_until(['db', 'database', 'get', '--database-id', vm_database_test_data_guard_with_new_db], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
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
    util.wait_until(['db', 'database', 'get', '--database-id', vm_database_test_data_guard_with_new_db], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
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
    util.wait_until(['db', 'database', 'get', '--database-id', vm_database_test_data_guard_with_new_db], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
    util.wait_until(['db', 'database', 'get', '--database-id', peer_database_id], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)

    # Delete the Data Guard Association By Termininating the DataGuard DB System.
    params = [
        'system', 'terminate',
        '--db-system-id', peer_db_system_id,
        '--force'
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    # validate that it goes into terminating state
    params = [
        'system', 'get',
        '--db-system-id', peer_db_system_id
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    state = json.loads(result.output)['data']['lifecycle-state']
    assert "TERMINAT" in state
    util.wait_until(['db', 'system', 'get', '--db-system-id', peer_db_system_id], 'TERMINATED', max_wait_seconds=DB_SYSTEM_PROVISIONING_TIME_SEC, succeed_if_not_found=True)
    util.wait_until(['db', 'system', 'get', '--db-system-id', vm_db_system_test_data_guard_with_new_db[0]], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)

    # LIST
    params = [
        'data-guard-association', 'list',
        '--database-id', vm_database_test_data_guard_with_new_db
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert len(json.loads(result.output)['data']) > 0
