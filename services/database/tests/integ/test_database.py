# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

'''
# These tests should now work collectively, this way:
# export CLI_TESTS_ADMIN_PASS_PHRASE="XXXXXXXX"
# pytest -s --enable-long-running --vcr-record-mode=none tests/test_database.py

# Or individually:
# pytest -s --enable-long-running --vcr-record-mode=none tests/test_database.py::test_list_db_systems
db_tests="test_list_db_systems test_list_db_system_shapes test_list_db_versions test_update_db_system test_data_guard_operations test_data_guard_with_new_db test_launch_db_from_database test_create_database_from_database test_database_operations test_backup_operations test_db_node_operations test_patch_operations test_patch_history_operations test_launch_exa_db_system"
for tfunc in ${db_tests};do
  pytest -s --enable-long-running --vcr-record-mode=none tests/test_database.py::${tfunc}
done
'''

import json
import oci
import oci_cli
import os
import pytest

from tests import util
from tests import test_config_container

ADMIN_PASSWORD = "BEstr0ng_#1"
DB_VERSION = '12.1.0.2'
DB_SYSTEM_CPU_CORE_COUNT = '4'
DB_RECOVERY_WINDOW = '45'
DB_SYSTEM_DB_EDITION = 'ENTERPRISE_EDITION'
DB_SYSTEM_DB_EXTREME_EDITION = 'ENTERPRISE_EDITION_EXTREME_PERFORMANCE'
DB_SYSTEM_SHAPE = 'BM.DenseIO2.52'
DB_SYSTEM_PROVISIONING_TIME_SEC = 14400  # 4 hours
DB_SYSTEM_UPDATE_TIME = 1800  # 30 minutes

DB_BACKUP_TIME_SEC = 7200  # 2 hours
DB_PROVISIONING_TIME_SEC = 1800  # 30 minutes
DB_TERMINATING_TIME_SEC = 1800  # 30 minutes
DB_PATCH_TIME_SEC = 900  # 15 minutes

DATA_GUARD_ASSOCIATION_OPERATION_TIME = 3600  # 60 minutes
DB_NODE_OPERATION_TIME = 1800  # 30 minutes

# if there are existing db systems, use those and bypass system creation
EXISTING_DB_SYSTEM_1 = os.environ.get('OCI_CLI_EXISTING_DB_SYSTEM_1')
EXISTING_DB_SYSTEM_2 = os.environ.get('OCI_CLI_EXISTING_DB_SYSTEM_2')
EXISTING_VM_DB_SYSTEM = os.environ.get('OCI_CLI_EXISTING_VM_DB_SYSTEM')
EXISTING_SUBNET = os.environ.get('OCI_CLI_EXISTING_SUBNET')

# by default clean up all resources. if OCI_CLI_SKIP_CLEAN_UP_DB_RESOURCES == '1' then do not clean up resources
SKIP_CLEAN_UP_RESOURCES = os.environ.get('OCI_CLI_SKIP_CLEAN_UP_DB_RESOURCES') == '1'
# This is useful for some local tesing scenarios.
ADDITIONAL_PARAMETERS = []
CASSETTE_LIBRARY_DIR = 'services/database/tests/cassettes'

# We are doing this b/c we have recent recordings with data for test_data_guard_with_new_db
# from our new tenancy, but still have old recordings and for the other tests.
# Unfortunately, at this time we don't have the proper limits to re-record the old tests.
match_on = ['method', 'scheme', 'vcr_host_matcher', 'port', 'vcr_path_matcher', 'vcr_query_matcher']


@pytest.fixture(autouse=True, scope='function')
def log_test(request):
    print("Test {name}...".format(name=request.function.__name__))
    yield
    print("Test {name} Complete".format(name=request.function.__name__))


# DBaaS test1

def test_list_db_systems(runner, config_file, config_profile):
    # other db system operations are covered by the db_system fixture (create, get, delete)
    params = [
        'system', 'list',
        '--compartment-id', util.COMPARTMENT_ID
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


# DBaaS test2

def test_list_db_system_shapes(runner, config_file, config_profile):
    # other db system operations are covered by the db_system fixture (create, get, delete)
    params = [
        'system-shape', 'list',
        '--availability-domain', util.availability_domain(),
        '--compartment-id', util.COMPARTMENT_ID
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # validate that we get back multiple shapes
    assert len(json.loads(result.output)['data']) > 0


# DBaaS test3

def test_list_db_versions(runner, config_file, config_profile):
    params = [
        'version', 'list',
        '--compartment-id', util.COMPARTMENT_ID
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # validate that we get back multiple versions
    assert len(json.loads(result.output)['data']) > 0


# DBaaS test4

@pytest.fixture(scope='module')
def networking_test_update_db_system(runner, config_file, config_profile, network_client, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_update_db_system_fixture.yml'):
        subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client)
        yield networking_dict

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_update_db_system_fixture_cleanup.yml'):
        networking_cleanup(network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


@pytest.fixture(scope='module')
def db_systems_test_update_db_system(runner, config_file, config_profile, networking_test_update_db_system, network_client, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_db_systems_test_update_db_system_fixture.yml'):
        db_system_id_1, db_system_id_2 = db_systems(runner, config_file, config_profile, networking_test_update_db_system, network_client, request)
        yield [db_system_id_1, db_system_id_2]

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_db_systems_test_update_db_system_fixture_cleanup.yml'):
        db_systems_cleanup(runner, config_file, config_profile, db_system_id_1, db_system_id_2)


@util.long_running
def test_update_db_system(runner, config_file, config_profile, db_systems_test_update_db_system):

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_update_db_system.yml'):
        params = [
            'system', 'update',
            '--db-system-id', db_systems_test_update_db_system[0],
            '--cpu-core-count', '6',
            '--ssh-authorized-keys-file', util.SSH_AUTHORIZED_KEYS_FILE,
            '--force'  # disable confirm prompt for overwriting ssh keys list
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        util.wait_until(['db', 'system', 'get', '--db-system-id', db_systems_test_update_db_system[0]], 'AVAILABLE', max_wait_seconds=DB_SYSTEM_UPDATE_TIME)

        # db system has updated so verify new fields
        params = [
            'system', 'get',
            '--db-system-id', db_systems_test_update_db_system[0]
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        json_result = json.loads(result.output)
        assert json_result['data']['cpu-core-count'] == 6

        print("Updated DB System: " + result.output)


# DBaaS test5
###########################
# DATA GUARD OPERATIONS
###########################


@pytest.fixture(scope='module')
def networking_test_data_guard_operations(runner, config_file, config_profile, network_client, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_data_guard_operations_fixture.yml'):
        subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client)
        yield networking_dict

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_data_guard_operations_fixture_cleanup.yml'):
        networking_cleanup(network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


@pytest.fixture(scope='module')
def db_systems_test_data_guard_operations(runner, config_file, config_profile, networking_test_data_guard_operations, network_client, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_db_systems_test_data_guard_operations_fixture.yml'):
        db_system_id_1, db_system_id_2 = db_systems(runner, config_file, config_profile, networking_test_data_guard_operations, network_client, request)
        yield [db_system_id_1, db_system_id_2]

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_db_systems_test_data_guard_operations_fixture_cleanup.yml'):
        db_systems_cleanup(runner, config_file, config_profile, db_system_id_1, db_system_id_2)


@pytest.fixture(scope='module')
def database_test_data_guard_operations(runner, config_file, config_profile, db_systems_test_data_guard_operations):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_database_test_data_guard_operations_fixture.yml'):
        return get_database(runner, config_file, config_profile, db_systems_test_data_guard_operations)


@util.long_running
def test_data_guard_operations(runner, config_file, config_profile, database_test_data_guard_operations, db_systems_test_data_guard_operations):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_data_guard_operations.yml'):
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
        print("Creating Data Guard Association...")
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


# DBaaS Test6

@pytest.fixture(scope='module')
def networking_test_data_guard_with_new_db(runner, config_file, config_profile, network_client, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_data_guard_with_new_db_fixture.yml'):
        subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client)
        yield networking_dict

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_data_guard_with_new_db_fixture_cleanup.yml'):
        networking_cleanup(network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


@pytest.fixture(scope='module')
def vm_db_system_test_data_guard_with_new_db(runner, config_file, config_profile, networking_test_data_guard_with_new_db, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_vm_db_system_test_data_guard_with_new_db_fixture.yml'):
        db_system_id_1 = vm_db_system(runner, config_file, config_profile, networking_test_data_guard_with_new_db, request)
        yield [db_system_id_1, ]

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_vm_db_system_test_data_guard_with_new_db_fixture_cleanup.yml'):
        vm_db_system_cleanup(runner, config_file, config_profile, db_system_id_1)


@pytest.fixture(scope='module')
def vm_database_test_data_guard_with_new_db(runner, config_file, config_profile, vm_db_system_test_data_guard_with_new_db):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_vm_database_test_data_guard_with_new_db_fixture.yml'):
        return get_database(runner, config_file, config_profile, vm_db_system_test_data_guard_with_new_db)


@util.long_running
def test_data_guard_with_new_db(runner, config_file, config_profile, vm_database_test_data_guard_with_new_db, vm_db_system_test_data_guard_with_new_db):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_data_guard_with_new_db.yml'):
        # Get the subnet of the existing database
        params = ['system', 'get', '--db-system-id', vm_db_system_test_data_guard_with_new_db[0]]
        result = invoke(runner, config_file, config_profile, params)
        subnet_id = json.loads(result.output)['data']['subnet-id']

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
            '--availability-domain', util.availability_domain(),
            '--display-name', 'DataGuardDb',
            # The combined hostname and domain cannot be longer than 56 characters.
            '--hostname', util.random_name('host', insert_underscore=False),
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


# DBaaS Test7

@pytest.fixture(scope='module')
def networking_test_launch_db_from_database(runner, config_file, config_profile, network_client, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_launch_db_from_database_fixture.yml'):
        subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client)
        yield networking_dict

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_launch_db_from_database_fixture_cleanup.yml'):
        networking_cleanup(network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


@pytest.fixture(scope='module')
def bm_db_system_test_launch_db_from_database(runner, config_file, config_profile, networking_test_launch_db_from_database, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_bm_db_system_test_launch_db_from_database_fixture.yml'):
        db_system_id_1 = bm_db_system(runner, config_file, config_profile, networking_test_launch_db_from_database, request)
        yield [db_system_id_1]

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_bm_db_system_test_launch_db_from_database_fixture_cleanup.yml'):
        bm_db_system_cleanup(runner, config_file, config_profile, db_system_id_1)


@pytest.fixture(scope='module')
def bm_database_test_launch_db_from_database(runner, config_file, config_profile, bm_db_system_test_launch_db_from_database):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_bm_database_test_launch_db_from_database_fixture.yml'):
        return get_database(runner, config_file, config_profile, bm_db_system_test_launch_db_from_database)


@util.long_running
@pytest.mark.skip(reason="launch-from-database not implemented")
def test_launch_db_from_database(runner, config_file, config_profile, bm_database_test_launch_db_from_database, bm_db_system_test_launch_db_from_database):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_launch_db_from_database.yml'):
        # There needs to be a backup created before doing launchDbSystem/createDbHome
        # 1) Enable Auto backups
        # 3) CreateBackup (since there is a bug in CP code. The bug has been fixed but not deployed yet.)
        # 4) Call launch-from-database
        shape = DB_SYSTEM_SHAPE
        compartment_id = util.COMPARTMENT_ID
        availability_domain = util.availability_domain()

        if EXISTING_SUBNET:
            subnet_id = EXISTING_SUBNET
        else:
            # Get the subnet of the existing database
            params = ['system', 'get', '--db-system-id', bm_db_system_test_launch_db_from_database[0]]
            result = invoke(runner, config_file, config_profile, params)
            subnet_id = json.loads(result.output)['data']['subnet-id']
            params.extend(ADDITIONAL_PARAMETERS)

        params = [
            'database', 'update',
            '--database-id', bm_database_test_launch_db_from_database,
            '--auto-backup-enabled', 'true',
            '--force'
        ]
        params.extend(ADDITIONAL_PARAMETERS)
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        params = [
            'backup', 'create',
            '--database-id', bm_database_test_launch_db_from_database,
            '--display-name', util.random_name('CliDbBackupDisplayName', insert_underscore=False)
        ]
        params.extend(ADDITIONAL_PARAMETERS)
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        wait_params = ['db', 'database', 'get', '--database-id', bm_database_test_launch_db_from_database]
        wait_params.extend(ADDITIONAL_PARAMETERS)
        util.wait_until(wait_params, 'AVAILABLE', max_wait_seconds=DB_PROVISIONING_TIME_SEC)

        params = [
            'system', 'launch-from-database',
            '--admin-password', ADMIN_PASSWORD,
            '--availability-domain', availability_domain,
            '--compartment-id', compartment_id,
            '--cpu-core-count', DB_SYSTEM_CPU_CORE_COUNT,
            '--database-edition', DB_SYSTEM_DB_EDITION,
            '--db-name', random_db_name(),
            '--display-name', util.random_name('CliDbSysDisplayName', insert_underscore=False),
            '--hostname', util.random_name('cli-test-hostname', insert_underscore=False),
            '--shape', shape,
            '--ssh-authorized-keys-file', util.SSH_AUTHORIZED_KEYS_FILE,
            '--subnet-id', subnet_id,
            '--license-model', 'LICENSE_INCLUDED',
            '--database-id', bm_database_test_launch_db_from_database,
            '--backup-tde-password', ADMIN_PASSWORD
        ]
        params.extend(ADDITIONAL_PARAMETERS)
        print("launch-from-database params=", params)
        result = invoke(runner, config_file, config_profile, params)
        print("launch-from-database result=", str(result))
        util.validate_response(result)
        print(str(result.output))

        json_result = json.loads(result.output)


# DBaaS test8

@pytest.fixture(scope='module')
def networking_test_create_database_from_database(runner, config_file, config_profile, network_client, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_create_database_from_database_fixture.yml'):
        subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client)
        yield networking_dict

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_create_database_from_database_cleanup.yml'):
        networking_cleanup(network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


@pytest.fixture(scope='module')
def bm_db_system_test_create_database_from_database(runner, config_file, config_profile, networking_test_create_database_from_database, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_bm_db_system_test_create_database_from_database_fixture.yml'):
        db_system_id_1 = bm_db_system(runner, config_file, config_profile, networking_test_create_database_from_database, request)
        yield [db_system_id_1]

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_bm_db_system_test_create_database_from_database_fixture_cleanup.yml'):
        bm_db_system_cleanup(runner, config_file, config_profile, db_system_id_1)


@pytest.fixture(scope='module')
def bm_database_test_create_database_from_database(runner, config_file, config_profile, bm_db_system_test_create_database_from_database):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_bm_database_test_create_database_from_database_fixture.yml'):
        return get_database(runner, config_file, config_profile, bm_db_system_test_create_database_from_database)


@util.long_running
@pytest.mark.skip(reason="create-from-database not implemented")
def test_create_database_from_database(runner, config_file, config_profile, bm_database_test_create_database_from_database, bm_db_system_test_create_database_from_database):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_create_database_from_database.yml'):
        # There needs to be a backup created before doing launchDbSystem/createDbHome
        # 1) Enable Auto backups
        # 3) CreateBackup (since there is a bug in CP code. The bug has been fixed but not deployed yet.)
        # 4) Call create-from-database
        shape = DB_SYSTEM_SHAPE
        compartment_id = util.COMPARTMENT_ID
        availability_domain = util.availability_domain()

        if EXISTING_SUBNET:
            subnet_id = EXISTING_SUBNET
        else:
            # Get the subnet of the existing database
            params = ['system', 'get', '--db-system-id', bm_db_system_test_create_database_from_database[0]]
            result = invoke(runner, config_file, config_profile, params)
            subnet_id = json.loads(result.output)['data']['subnet-id']
            params.extend(ADDITIONAL_PARAMETERS)

        params = [
            'database', 'update',
            '--database-id', bm_database_test_create_database_from_database,
            '--auto-backup-enabled', 'true',
            '--force'
        ]
        params.extend(ADDITIONAL_PARAMETERS)
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        params = [
            'backup', 'create',
            '--database-id', bm_database_test_create_database_from_database,
            '--display-name', util.random_name('CliDbBackupDisplayName', insert_underscore=False)
        ]
        params.extend(ADDITIONAL_PARAMETERS)
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        wait_params = ['db', 'database', 'get', '--database-id', bm_database_test_create_database_from_database]
        wait_params.extend(ADDITIONAL_PARAMETERS)
        util.wait_until(wait_params, 'AVAILABLE', max_wait_seconds=DB_PROVISIONING_TIME_SEC)

        params = [
            'database', 'create-from-database',
            '--db-name', random_db_name(),
            '--db-system-id', bm_db_system_test_create_database_from_database[0],
            '--database-id', bm_database_test_create_database_from_database,
            '--admin-password', ADMIN_PASSWORD,
            '--backup-tde-password', ADMIN_PASSWORD
        ]
        params.extend(ADDITIONAL_PARAMETERS)
        print("create-from-database params=", params)
        result = invoke(runner, config_file, config_profile, params)
        print("create-from-database result=", str(result))
        util.validate_response(result)
        print(str(result.output))

        json_result = json.loads(result.output)


# DBaaS Test9

@pytest.fixture(scope='module')
def networking_test_database_operations(runner, config_file, config_profile, network_client, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_database_operations.yml'):
        subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client)
        yield networking_dict

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_database_operations_fixture_cleanup.yml'):
        networking_cleanup(network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


@pytest.fixture(scope='module')
def db_systems_test_database_operations(runner, config_file, config_profile, networking_test_database_operations, network_client, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_db_systems_test_database_operations_fixture.yml'):
        db_system_id_1, db_system_id_2 = db_systems(runner, config_file, config_profile, networking_test_database_operations, network_client, request)
        yield [db_system_id_1, db_system_id_2]

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_db_systems_test_database_operations_fixture_cleanup.yml'):
        db_systems_cleanup(runner, config_file, config_profile, db_system_id_1, db_system_id_2)


@util.long_running
def test_database_operations(runner, config_file, config_profile, db_systems_test_database_operations):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_database_operations.yml'):
        # create database
        params = [
            'database', 'create',
            '--db-system-id', db_systems_test_database_operations[0],
            '--db-version', DB_VERSION,
            '--admin-password', ADMIN_PASSWORD,
            '--recovery-window-in-days', DB_RECOVERY_WINDOW,
            '--db-name', random_db_name()
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        json_result = json.loads(result.output)
        database_id = json_result['data']['id']

        # get database
        util.wait_until(['db', 'database', 'get', '--database-id', database_id], 'AVAILABLE', max_wait_seconds=DB_PROVISIONING_TIME_SEC)

        # list databases
        params = [
            'database', 'list',
            '--compartment-id', util.COMPARTMENT_ID,
            '--db-system-id', db_systems_test_database_operations[0]
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # list databases with --limit 0
        params = [
            'database', 'list',
            '--compartment-id', util.COMPARTMENT_ID,
            '--db-system-id', db_systems_test_database_operations[0],
            '--limit', '0'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(result.output) == 0

        # update database
        params = [
            'database', 'update',
            '--database-id', database_id,
            '--auto-backup-enabled', 'true',
            '--recovery-window-in-days', DB_RECOVERY_WINDOW,
            '--force'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        json_result = json.loads(result.output)
        assert json_result['data']['db-backup-config']['auto-backup-enabled'] is True

        util.wait_until(['db', 'database', 'get', '--database-id', database_id], 'AVAILABLE', max_wait_seconds=DB_PROVISIONING_TIME_SEC)

        # delete database
        params = [
            'database', 'delete',
            '--database-id', database_id,
            '--force'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        util.wait_until(['db', 'database', 'get', '--database-id', database_id], 'TERMINATED', max_wait_seconds=DB_TERMINATING_TIME_SEC, succeed_if_not_found=True)
        util.wait_until(['db', 'system', 'get', '--db-system-id', db_systems_test_database_operations[0]], 'AVAILABLE', max_wait_seconds=DB_TERMINATING_TIME_SEC)


# DBaaS Test10

@pytest.fixture(scope='module')
def networking_test_backup_operations(runner, config_file, config_profile, network_client, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_backup_operations_fixture.yml'):
        subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client)
        yield networking_dict

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_backup_operations_fixture_cleanup.yml'):
        networking_cleanup(network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


@pytest.fixture(scope='module')
def db_systems_test_backup_operations(runner, config_file, config_profile, networking_test_backup_operations, network_client, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_db_systems_test_backup_operations_fixture.yml'):
        db_system_id_1, db_system_id_2 = db_systems(runner, config_file, config_profile, networking_test_backup_operations, network_client, request)
        yield [db_system_id_1, db_system_id_2]

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_db_systems_test_backup_operations_fixture_cleanup.yml'):
        db_systems_cleanup(runner, config_file, config_profile, db_system_id_1, db_system_id_2)


@pytest.fixture(scope='module')
def database_test_backup_operations(runner, config_file, config_profile, db_systems_test_backup_operations):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_database_test_backup_operations_fixture.yml'):
        return get_database(runner, config_file, config_profile, db_systems_test_backup_operations)


@util.long_running
def test_backup_operations(runner, config_file, config_profile, db_systems_test_backup_operations, database_test_backup_operations):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_backup_operations.yml'):
        # create backup
        print("Creating backup..")
        params = [
            'backup', 'create',
            '--database-id', database_test_backup_operations,
            '--display-name', util.random_name('CliDbBackup')
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        json_result = json.loads(result.output)
        backup_id = json_result['data']['id']

        # get backup
        print("Getting backup..")
        util.wait_until(['db', 'backup', 'get', '--backup-id', backup_id], 'ACTIVE', max_wait_seconds=DB_BACKUP_TIME_SEC)

        # list backups by database
        params = [
            'backup', 'list',
            '--database-id', database_test_backup_operations
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        print(result.output)
        assert len(json.loads(result.output)['data']) > 0

        # list backups by compartment
        params = [
            'backup', 'list',
            '--compartment-id', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        print(result.output)
        assert len(json.loads(result.output)['data']) > 0

        # restore from backup
        params = [
            'database', 'restore',
            '--database-id', database_test_backup_operations,
            '--latest', 'true'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        util.wait_until(['db', 'database', 'get', '--database-id', database_test_backup_operations], 'AVAILABLE', max_wait_seconds=DB_BACKUP_TIME_SEC)

        # in order to create from backup we have to delete this database
        print("Deleting database in order to create from backup...")
        params = [
            'database', 'delete',
            '--database-id', database_test_backup_operations,
            '--force'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        util.wait_until(['db', 'database', 'get', '--database-id', database_test_backup_operations], 'TERMINATED', max_wait_seconds=DB_TERMINATING_TIME_SEC, succeed_if_not_found=True)
        util.wait_until(['db', 'system', 'get', '--db-system-id', db_systems_test_backup_operations[0]], 'AVAILABLE', max_wait_seconds=DB_TERMINATING_TIME_SEC)

        # create from backup
        params = [
            'database', 'create-from-backup',
            '--db-system-id', db_systems_test_backup_operations[0],
            '--backup-id', backup_id,
            '--admin-password', ADMIN_PASSWORD,
            '--db-name', 'renameDb',
            '--backup-tde-password', ADMIN_PASSWORD
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        db_created_from_backup = json.loads(result.output)['data']['id']

        util.wait_until(['db', 'database', 'get', '--database-id', db_created_from_backup], 'AVAILABLE', max_wait_seconds=DB_PROVISIONING_TIME_SEC)
        print("Restored Database with a new database name")

        params = [
            'system', 'get',
            '--db-system-id', db_systems_test_backup_operations[0]
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        subnet = json.loads(result.output)['data']['subnet-id']

        print("Launching new Dbsystem from backup with renamed database ")
        # Launch dbsystem
        params_1 = [
            'system', 'launch-from-backup',
            '--ssh-authorized-keys-file', util.SSH_AUTHORIZED_KEYS_FILE,
            '--backup-id', backup_id,
            '--subnet-id', subnet,
            '--hostname', util.random_name('cli-test-hostname', insert_underscore=False),
            '--db-name', 'renameDb',
            '--availability-domain', util.availability_domain(),
            '--shape', DB_SYSTEM_SHAPE,
            '--display-name', util.random_name('CliDbSysDisplayName', insert_underscore=False),
            '--initial-data-storage-size-in-gb', '256',
            '--compartment-id', util.COMPARTMENT_ID,
            '--admin-password', ADMIN_PASSWORD,
            '--backup-tde-password', ADMIN_PASSWORD,
            '--cpu-core-count', '4',
            '--database-edition', DB_SYSTEM_DB_EXTREME_EDITION
        ]
        result = invoke(runner, config_file, config_profile, params_1)
        util.validate_response(result)
        dbsystem_from_backup = json.loads(result.output)['data']['id']
        print("New dbsystem ocid:", dbsystem_from_backup)

        util.wait_until(['db', 'system', 'get', '--db-system-id', dbsystem_from_backup], 'AVAILABLE', max_wait_seconds=DB_SYSTEM_PROVISIONING_TIME_SEC)
        print("DB Systems provisioned successfully!")

        # delete backup
        print("Deleting backup")
        params = [
            'backup', 'delete',
            '--backup-id', backup_id,
            '--force'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        util.wait_until(['db', 'backup', 'get', '--backup-id', backup_id], 'TERMINATED', max_wait_seconds=DB_PROVISIONING_TIME_SEC, succeed_if_not_found=True)

        print("Deleting dbsystem")
        params = [
            'system', 'terminate',
            '--db-system-id', dbsystem_from_backup,
            '--force'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        util.wait_until(['db', 'system', 'get', '--db-system-id', dbsystem_from_backup], 'TERMINATED',
                        max_wait_seconds=DB_SYSTEM_PROVISIONING_TIME_SEC)
        print("backup test ends")


# DBaaS Test11

@pytest.fixture(scope='module')
def networking_test_db_node_operations(runner, config_file, config_profile, network_client, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_db_node_operations.yml'):
        subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client)
        yield networking_dict

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_db_node_operations_fixture_cleanup.yml'):
        networking_cleanup(network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


@pytest.fixture(scope='module')
def db_systems_test_db_node_operations(runner, config_file, config_profile, networking_test_db_node_operations, network_client, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_db_systems_test_db_node_operations_fixture.yml'):
        db_system_id_1, db_system_id_2 = db_systems(runner, config_file, config_profile, networking_test_db_node_operations, network_client, request)
        yield [db_system_id_1, db_system_id_2]

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_db_systems_test_db_node_operations_fixture_cleanup.yml'):
        db_systems_cleanup(runner, config_file, config_profile, db_system_id_1, db_system_id_2)


@util.long_running
def test_db_node_operations(runner, config_file, config_profile, db_systems_test_db_node_operations):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_db_node_operations.yml'):
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


# DBaaS Test12
###########################
# PATCH OPERATIONS
###########################

@pytest.fixture(scope='module')
def networking_test_patch_operations(runner, config_file, config_profile, network_client, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_patch_operations_fixture.yml'):
        subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client)
        yield networking_dict

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_patch_operations_fixture_cleanup.yml'):
        networking_cleanup(network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


@pytest.fixture(scope='module')
def db_systems_test_patch_operations(runner, config_file, config_profile, networking_test_patch_operations, network_client, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_db_systems_test_patch_operations_fixture.yml'):
        db_system_id_1, db_system_id_2 = db_systems(runner, config_file, config_profile, networking_test_patch_operations, network_client, request)
        yield [db_system_id_1, db_system_id_2]

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_db_systems_test_patch_operations_fixture_cleanup.yml'):
        db_systems_cleanup(runner, config_file, config_profile, db_system_id_1, db_system_id_2)


@pytest.fixture(scope='module')
def database_test_patch_operations(runner, config_file, config_profile, db_systems_test_patch_operations):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_database_test_patch_operations_fixture.yml'):
        return get_database(runner, config_file, config_profile, db_systems_test_patch_operations)


@util.long_running
def test_patch_operations(runner, config_file, config_profile, database_test_patch_operations, db_systems_test_patch_operations):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_patch_operations.yml'):
        # by db-system
        params = [
            'patch', 'list', 'by-db-system',
            '--db-system-id', db_systems_test_patch_operations[0]
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        if len(result.output) > 0:
            json_result = json.loads(result.output)
            if len(json_result['data']) > 0:
                patch_id = json_result['data'][0]['id']
                print("Getting patch {} for db system {}".format(patch_id, db_systems_test_patch_operations[0]))

                params = [
                    'patch', 'get', 'by-db-system',
                    '--db-system-id', db_systems_test_patch_operations[0],
                    '--patch-id', patch_id
                ]

                result = invoke(runner, config_file, config_profile, params)
                util.validate_response(result)

                json_result = json.loads(result.output)
                if 'APPLY' in json_result['data']['available-actions']:
                    print('Applying patch: {} to db system: {}'.format(patch_id, db_systems_test_patch_operations[0]))

                    params = [
                        'db-system', 'patch',
                        '--db-system-id', db_systems_test_patch_operations[0],
                        '--patch-id', patch_id,
                        '--patch-action', 'APPLY'
                    ]

                    result = invoke(runner, config_file, config_profile, params)
                    util.validate_response(result)

                    util.wait_until(['db', 'system', 'get', '--db-system-id', db_systems_test_patch_operations[0]], 'AVAILABLE', max_wait_seconds=DB_PATCH_TIME_SEC)

        # by database
        params = [
            'patch', 'list', 'by-database',
            '--database-id', database_test_patch_operations
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        if len(result.output) > 0:
            json_result = json.loads(result.output)
            if len(json_result['data']) > 0:
                patch_id = json_result['data'][0]['id']
                print("Getting patch {} for database {}".format(patch_id, database_test_patch_operations))

                params = [
                    'patch', 'get', 'by-database',
                    '--database-id', database_test_patch_operations,
                    '--patch-id', patch_id
                ]

                result = invoke(runner, config_file, config_profile, params)
                util.validate_response(result)

                json_result = json.loads(result.output)
                if 'APPLY' in json_result['data']['available-actions']:
                    print('Applying patch: {} to database: {}'.format(patch_id, database_test_patch_operations))

                    params = [
                        'database', 'patch',
                        '--database-id', database_test_patch_operations,
                        '--patch-id', patch_id,
                        '--patch-action', 'APPLY'
                    ]

                    result = invoke(runner, config_file, config_profile, params)
                    util.validate_response(result)

                    util.wait_until(['db', 'database', 'get', '--database-id', database_test_patch_operations], 'AVAILABLE', max_wait_seconds=DB_PATCH_TIME_SEC)


# DBaaS Test13
###########################
# PATCH HISTORY OPERATIONS
###########################

@pytest.fixture(scope='module')
def networking_test_patch_history_operations(runner, config_file, config_profile, network_client, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_patch_history_operations_fixture.yml'):
        subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client)
        yield networking_dict

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_patch_history_operations_fixture_cleanup.yml'):
        networking_cleanup(network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


@pytest.fixture(scope='module')
def db_systems_test_patch_history_operations(runner, config_file, config_profile, networking_test_patch_history_operations, network_client, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_db_systems_test_patch_history_operations_fixture.yml'):
        db_system_id_1, db_system_id_2 = db_systems(runner, config_file, config_profile, networking_test_patch_history_operations, network_client, request)
        yield [db_system_id_1, db_system_id_2]

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_db_systems_test_patch_history_operations_fixture_cleanup.yml'):
        db_systems_cleanup(runner, config_file, config_profile, db_system_id_1, db_system_id_2)


@pytest.fixture(scope='module')
def database_test_patch_history_operations(runner, config_file, config_profile, db_systems_test_patch_history_operations):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_database_test_patch_history_operations_fixture.yml'):
        return get_database(runner, config_file, config_profile, db_systems_test_patch_history_operations)


@util.long_running
def test_patch_history_operations(runner, config_file, config_profile, database_test_patch_history_operations, db_systems_test_patch_history_operations):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_patch_history_operations.yml'):
        # by db-system
        params = [
            'patch-history', 'list', 'by-db-system',
            '--db-system-id', db_systems_test_patch_history_operations[0]
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        if len(result.output) > 0:
            json_result = json.loads(result.output)
            if len(json_result['data']) > 0:
                patch_history_entry_id = json_result['data'][0]['id']

                params = [
                    'patch-history', 'get', 'by-db-system',
                    '--db-system-id', db_systems_test_patch_history_operations[0],
                    '--patch-history-entry-id', patch_history_entry_id
                ]

                result = invoke(runner, config_file, config_profile, params)
                util.validate_response(result)

        # by database
        params = [
            'patch-history', 'list', 'by-database',
            '--database-id', database_test_patch_history_operations
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        if len(result.output) > 0:
            json_result = json.loads(result.output)
            if len(json_result['data']) > 0:
                patch_history_entry_id = json_result['data'][0]['id']

                params = [
                    'patch-history', 'get', 'by-database',
                    '--database-id', database_test_patch_history_operations,
                    '--patch-history-entry-id', patch_history_entry_id
                ]

                result = invoke(runner, config_file, config_profile, params)
                util.validate_response(result)


# DBaaS Test14

@pytest.fixture(scope='module')
def networking_test_launch_exa_db_system(runner, config_file, config_profile, network_client, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_launch_exa_db_system_fixture.yml'):
        subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client)
        yield networking_dict

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('database_networking_test_launch_exa_db_system_fixture_cleanup.yml'):
        networking_cleanup(network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


def test_launch_exa_db_system(runner, config_file, config_profile, networking_test_launch_exa_db_system):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_launch_exa_db_system.yml'):
        DB_SYSTEM_SHAPE = 'Exadata.Quarter2.92'

        # provision DB systems
        params = [
            'system', 'launch',
            '--admin-password', ADMIN_PASSWORD,
            '--availability-domain', util.availability_domain(),
            '--compartment-id', util.COMPARTMENT_ID,
            '--cpu-core-count', DB_SYSTEM_CPU_CORE_COUNT,
            '--database-edition', DB_SYSTEM_DB_EXTREME_EDITION,
            '--db-name', random_db_name(),
            '--db-version', DB_VERSION,
            '--display-name', util.random_name('CliDbSys', insert_underscore=False),
            '--hostname', util.random_name('clihnm', insert_underscore=False),
            '--shape', DB_SYSTEM_SHAPE,
            '--ssh-authorized-keys-file', util.SSH_AUTHORIZED_KEYS_FILE,
            '--subnet-id', networking_test_launch_exa_db_system['subnet_ocid_1'],
            '--backup-subnet-id', networking_test_launch_exa_db_system['subnet_ocid_2'],
            '--sparse-diskgroup', 'true'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        print(str(result.output))

        json_result = json.loads(result.output)
        db_system_id_1 = json_result['data']['id']

        print("Wating for DB System to launch...")

        # launch db system
        util.wait_until(['db', 'system', 'get', '--db-system-id', db_system_id_1], 'PROVISIONING', max_wait_seconds=DB_SYSTEM_PROVISIONING_TIME_SEC)
        print("DB System launched successfully!")

        if SKIP_CLEAN_UP_RESOURCES:
            print("Skipping clean up of DB systems and dependent resources.")
            return

        success_terminating_db_systems = True

        try:
            # terminate db system
            params = [
                'system', 'terminate',
                '--db-system-id', db_system_id_1,
                '--force'
            ]
            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result)

            # validate that it goes into terminating state
            params = [
                'system', 'get',
                '--db-system-id', db_system_id_1
            ]
            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result)

            state = json.loads(result.output)['data']['lifecycle-state']
            assert "TERMINAT" in state
            # TODO: Re-enable this after this is re-recorded using CLI tenancy.
            util.wait_until(['db', 'system', 'get', '--db-system-id', db_system_id_1], 'TERMINATED', max_wait_seconds=DB_SYSTEM_PROVISIONING_TIME_SEC, succeed_if_not_found=True)
        except Exception as error:
            util.print_latest_exception(error)
            success_terminating_db_systems = False

        assert success_terminating_db_systems


# Common functions used in tests

@pytest.fixture(scope='module')
def bm_db_system(runner, config_file, config_profile, networking, request):
    DB_SYSTEM_SHAPE = "BM.DenseIO2.52"
    if EXISTING_DB_SYSTEM_1:
        return [EXISTING_DB_SYSTEM_1]
    else:
        # provision DB systems
        params = [
            'system', 'launch',
            '--admin-password', ADMIN_PASSWORD,
            '--availability-domain', util.availability_domain(),
            '--compartment-id', util.COMPARTMENT_ID,
            '--cpu-core-count', DB_SYSTEM_CPU_CORE_COUNT,
            '--database-edition', DB_SYSTEM_DB_EDITION,
            '--db-name', random_db_name(),
            '--db-version', DB_VERSION,
            '--display-name', util.random_name('CliDbSysDisplayName', insert_underscore=False),
            '--hostname', util.random_name('cli-test-hostname', insert_underscore=False),
            '--shape', DB_SYSTEM_SHAPE,
            '--ssh-authorized-keys-file', util.SSH_AUTHORIZED_KEYS_FILE,
            '--subnet-id', networking['subnet_ocid_1'],
            '--license-model', 'LICENSE_INCLUDED',
            '--node-count', '1',
            '--initial-data-storage-size-in-gb', '256'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        print(str(result.output))

        json_result = json.loads(result.output)
        db_system_id_1 = json_result['data']['id']

        print("Wating for DB System to complete provisioning...")

        # create db system and wait to finish
        util.wait_until(['db', 'system', 'get', '--db-system-id', db_system_id_1], 'AVAILABLE', max_wait_seconds=DB_SYSTEM_PROVISIONING_TIME_SEC)
        print("bm_db_system: DB System provisioned successfully!")
        return db_system_id_1


def bm_db_system_cleanup(runner, config_file, config_profile, db_system_id_1):

    if SKIP_CLEAN_UP_RESOURCES:
        print("Skipping clean up of DB systems and dependent resources.")
        return

    success_terminating_db_systems = True

    try:
        # terminate db system 1
        params = [
            'system', 'terminate',
            '--db-system-id', db_system_id_1,
            '--force'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # validate that it goes into terminating state
        params = [
            'system', 'get',
            '--db-system-id', db_system_id_1
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        state = json.loads(result.output)['data']['lifecycle-state']
        assert "TERMINAT" in state
        util.wait_until(['db', 'system', 'get', '--db-system-id', db_system_id_1], 'TERMINATED',
                        max_wait_seconds=DB_SYSTEM_PROVISIONING_TIME_SEC, succeed_if_not_found=True)
    except Exception as error:
        util.print_latest_exception(error)
        success_terminating_db_systems = False

    assert success_terminating_db_systems


def vm_db_system(runner, config_file, config_profile, networking, request):
    DB_SYSTEM_SHAPE = 'VM.Standard2.1'
    if EXISTING_VM_DB_SYSTEM:
        return [EXISTING_VM_DB_SYSTEM, ]
    else:
        # provision DB systems
        params = [
            'system', 'launch',
            '--admin-password', ADMIN_PASSWORD,
            '--availability-domain', util.availability_domain(),
            '--compartment-id', util.COMPARTMENT_ID,
            '--cpu-core-count', DB_SYSTEM_CPU_CORE_COUNT,
            '--database-edition', DB_SYSTEM_DB_EDITION,
            '--db-name', random_db_name(),
            '--db-version', DB_VERSION,
            '--display-name', util.random_name('CliDbSysDisplayName', insert_underscore=False),
            '--hostname', util.random_name('cli-test-hostname', insert_underscore=False),
            '--shape', DB_SYSTEM_SHAPE,
            '--ssh-authorized-keys-file', util.SSH_AUTHORIZED_KEYS_FILE,
            '--subnet-id', networking['subnet_ocid_1'],
            '--license-model', 'LICENSE_INCLUDED',
            '--node-count', '1',
            '--initial-data-storage-size-in-gb', '256'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        print(str(result.output))

        json_result = json.loads(result.output)
        db_system_id_1 = json_result['data']['id']

        print("Wating for DB System to complete provisioning...")

        # create db system and wait to finish
        util.wait_until(['db', 'system', 'get', '--db-system-id', db_system_id_1], 'AVAILABLE', max_wait_seconds=DB_SYSTEM_PROVISIONING_TIME_SEC)
        print("vm_db_system: DB System provisioned successfully!")
        return db_system_id_1


def vm_db_system_cleanup(runner, config_file, config_profile, db_system_id_1):
    if SKIP_CLEAN_UP_RESOURCES:
        print("Skipping clean up of DB systems and dependent resources.")
        return

    success_terminating_db_systems = True

    try:
        # terminate db system 1
        params = [
            'system', 'terminate',
            '--db-system-id', db_system_id_1,
            '--force'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # validate that it goes into terminating state
        params = [
            'system', 'get',
            '--db-system-id', db_system_id_1
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        state = json.loads(result.output)['data']['lifecycle-state']
        assert "TERMINAT" in state
        util.wait_until(['db', 'system', 'get', '--db-system-id', db_system_id_1], 'TERMINATED', max_wait_seconds=DB_SYSTEM_PROVISIONING_TIME_SEC, succeed_if_not_found=True)
    except Exception as error:
        util.print_latest_exception(error)
        success_terminating_db_systems = False

    assert success_terminating_db_systems


def db_systems(runner, config_file, config_profile, networking, network_client, request):
    # allow running against existing DB systems instead of launching new ones to save time
    if EXISTING_DB_SYSTEM_1 and EXISTING_DB_SYSTEM_2:
        return EXISTING_DB_SYSTEM_1, EXISTING_DB_SYSTEM_2
    else:
        # provision DB systems
        # Get AD of subnet
        subnet_response = network_client.get_subnet(networking['subnet_ocid_1'])
        print("Using subnet's AD", subnet_response.data.availability_domain)
        params = [
            'system', 'launch',
            '--admin-password', ADMIN_PASSWORD,
            '--availability-domain', subnet_response.data.availability_domain,
            '--compartment-id', util.COMPARTMENT_ID,
            '--cpu-core-count', DB_SYSTEM_CPU_CORE_COUNT,
            '--database-edition', DB_SYSTEM_DB_EDITION,
            '--db-name', random_db_name(),
            '--db-version', DB_VERSION,
            '--display-name', util.random_name('CliDbSysDisplayName', insert_underscore=False),
            '--hostname', util.random_name('cli-test-hostname', insert_underscore=False),
            '--shape', DB_SYSTEM_SHAPE,
            '--ssh-authorized-keys-file', util.SSH_AUTHORIZED_KEYS_FILE,
            '--subnet-id', networking['subnet_ocid_1'],
            '--license-model', 'LICENSE_INCLUDED',
            '--node-count', '1',
            '--initial-data-storage-size-in-gb', '256',
            '--fault-domains', '["FAULT-DOMAIN-1"]'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        print(str(result.output))

        json_result = json.loads(result.output)
        db_system_id_1 = json_result['data']['id']

        subnet_response_2 = network_client.get_subnet(networking['subnet_ocid_2'])
        print("Using subnet's AD", subnet_response_2.data.availability_domain)

        params = [
            'system', 'launch',
            '--admin-password', ADMIN_PASSWORD,
            '--availability-domain', subnet_response_2.data.availability_domain,
            '--compartment-id', util.COMPARTMENT_ID,
            '--cpu-core-count', DB_SYSTEM_CPU_CORE_COUNT,
            '--database-edition', DB_SYSTEM_DB_EDITION,
            '--db-name', random_db_name(),
            '--db-version', DB_VERSION,
            '--display-name', util.random_name('CliDbSysDisplayName', insert_underscore=False),
            '--hostname', util.random_name('cli-test-hostname', insert_underscore=False),
            '--shape', DB_SYSTEM_SHAPE,
            '--ssh-authorized-keys-file', util.SSH_AUTHORIZED_KEYS_FILE,
            '--subnet-id', networking['subnet_ocid_2'],
            '--license-model', 'LICENSE_INCLUDED',
            '--node-count', '1',
            '--initial-data-storage-size-in-gb', '256',
            '--fault-domains', '["FAULT-DOMAIN-2"]'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        print(str(result.output))

        json_result = json.loads(result.output)
        db_system_id_2 = json_result['data']['id']

        print("Wating for DB Systems to complete provisioning...")

        # create db systems in parallel, then wait for both to finish
        util.wait_until(['db', 'system', 'get', '--db-system-id', db_system_id_1], 'AVAILABLE', max_wait_seconds=DB_SYSTEM_PROVISIONING_TIME_SEC)
        util.wait_until(['db', 'system', 'get', '--db-system-id', db_system_id_2], 'AVAILABLE', max_wait_seconds=DB_SYSTEM_PROVISIONING_TIME_SEC)
        print("DB Systems provisioned successfully!")
        return db_system_id_1, db_system_id_2


def db_systems_cleanup(runner, config_file, config_profile, db_system_id_1, db_system_id_2):
    if SKIP_CLEAN_UP_RESOURCES:
        print("Skipping clean up of DB systems and dependent resources.")
        return

    success_terminating_db_systems = True

    try:
        # terminate db system 1
        params = [
            'system', 'terminate',
            '--db-system-id', db_system_id_1,
            '--force'
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # validate that it goes into terminating state
        params = [
            'system', 'get',
            '--db-system-id', db_system_id_1
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        state = json.loads(result.output)['data']['lifecycle-state']
        assert "TERMINAT" in state
        util.wait_until(['db', 'system', 'get', '--db-system-id', db_system_id_1], 'TERMINATED',
                        max_wait_seconds=DB_SYSTEM_PROVISIONING_TIME_SEC, succeed_if_not_found=True)
    except Exception as error:
        util.print_latest_exception(error)
        success_terminating_db_systems = False

    # terminate db system 2
    try:
        params = [
            'system', 'terminate',
            '--db-system-id', db_system_id_2,
            '--force'
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # validate that it goes into terminating state
        params = [
            'system', 'get',
            '--db-system-id', db_system_id_2
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        state = json.loads(result.output)['data']['lifecycle-state']
        assert "TERMINAT" in state
        util.wait_until(['db', 'system', 'get', '--db-system-id', db_system_id_2], 'TERMINATED',
                        max_wait_seconds=DB_SYSTEM_PROVISIONING_TIME_SEC, succeed_if_not_found=True)
    except Exception as error:
        util.print_latest_exception(error)
        success_terminating_db_systems = False

    assert success_terminating_db_systems


def networking(network_client):
    if EXISTING_SUBNET:
        print("Returning existing subnet")
        networking_dict = {}
        networking_dict['vcn_ocid'] = ''
        networking_dict['subnet_ocid_1'] = EXISTING_SUBNET
        networking_dict['subnet_ocid_2'] = ''
        return EXISTING_SUBNET, "", "", "", "", networking_dict
    else:
        # create VCN
        print("Creating a new subnet")
        vcn_name = util.random_name('cli_db_test_vcn')
        cidr_block = "10.0.0.0/16"
        vcn_dns_label = util.random_name('vcn', insert_underscore=False)

        create_vcn_details = oci.core.models.CreateVcnDetails()
        create_vcn_details.cidr_block = cidr_block
        create_vcn_details.display_name = vcn_name
        create_vcn_details.compartment_id = util.COMPARTMENT_ID
        print("Compartment ID:", create_vcn_details.compartment_id)
        create_vcn_details.dns_label = vcn_dns_label

        result = network_client.create_vcn(create_vcn_details)
        vcn_ocid = result.data.id
        assert result.status == 200

        oci.wait_until(network_client, network_client.get_vcn(vcn_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

        # create subnet in first AD
        subnet_dns_label = util.random_name('subnet', insert_underscore=False) + '1'
        subnet_ocid_1 = create_subnet("10.0.1.0/24", subnet_dns_label, vcn_ocid, network_client)

        # create subnet in second AD
        subnet_dns_label = util.random_name('subnet', insert_underscore=False) + '2'
        subnet_ocid_2 = create_subnet("10.0.0.0/24", subnet_dns_label, vcn_ocid, network_client)

        # open up security list to allow data guard operations
        response = network_client.list_security_lists(util.COMPARTMENT_ID, vcn_ocid)

        # we just created this VCN so assume there is only one security list and it is the default
        default_security_list = response.data[0]

        # add new permissive ingress security rule
        new_allow_all_ingress_rule = oci.core.models.IngressSecurityRule()
        new_allow_all_ingress_rule.is_stateless = False
        new_allow_all_ingress_rule.protocol = "all"
        new_allow_all_ingress_rule.source = "0.0.0.0/0"

        default_security_list.ingress_security_rules.append(new_allow_all_ingress_rule)

        new_allow_all_egress_rule = oci.core.models.EgressSecurityRule()
        new_allow_all_egress_rule.destination = "0.0.0.0/0"
        new_allow_all_egress_rule.protocol = "all"
        new_allow_all_egress_rule.is_stateless = False

        default_security_list.egress_security_rules.append(new_allow_all_egress_rule)

        update_security_list_details = oci.core.models.UpdateSecurityListDetails()
        update_security_list_details.egress_security_rules = default_security_list.egress_security_rules
        update_security_list_details.ingress_security_rules = default_security_list.ingress_security_rules

        network_client.update_security_list(default_security_list.id, update_security_list_details)

        # create internet gateway
        create_ig_details = oci.core.models.CreateInternetGatewayDetails()
        create_ig_details.compartment_id = util.COMPARTMENT_ID
        create_ig_details.is_enabled = True
        create_ig_details.display_name = util.random_name('cli_db_ig')
        create_ig_details.vcn_id = vcn_ocid

        response = network_client.create_internet_gateway(create_ig_details)
        ig_ocid = response.data.id

        # add rule targeting internet gateway to default route table (first and only route table in list)
        response = network_client.list_route_tables(util.COMPARTMENT_ID, vcn_ocid)
        default_route_table = response.data[0]

        new_route_rule = oci.core.models.RouteRule()
        new_route_rule.cidr_block = '0.0.0.0/0'
        new_route_rule.network_entity_id = ig_ocid

        if not default_route_table.route_rules:
            default_route_table.route_rules = []

        default_route_table.route_rules.append(new_route_rule)

        update_route_table_details = oci.core.models.UpdateRouteTableDetails()
        update_route_table_details.route_rules = default_route_table.route_rules
        network_client.update_route_table(default_route_table.id, update_route_table_details)

        networking_dict = {}
        networking_dict['vcn_ocid'] = vcn_ocid
        networking_dict['subnet_ocid_1'] = subnet_ocid_1
        networking_dict['subnet_ocid_2'] = subnet_ocid_2
        return subnet_ocid_1, subnet_ocid_2, default_route_table.id, ig_ocid, vcn_ocid, networking_dict


def networking_cleanup(network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid):
        if SKIP_CLEAN_UP_RESOURCES:
            print("Skipping clean up of DB systems and dependent resources.")
            return

        success_terminating_db_systems = True

        try:
            # delete VCN and subnets now that dependent DB systems are deleted
            network_client.delete_subnet(subnet_ocid_1)

            try:
                oci.wait_until(network_client, network_client.get_subnet(subnet_ocid_1), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except oci.exceptions.ServiceError as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)

            network_client.delete_subnet(subnet_ocid_2)
            try:
                oci.wait_until(network_client, network_client.get_subnet(subnet_ocid_2), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except oci.exceptions.ServiceError as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)

            route_rules = []
            update_route_table_details = oci.core.models.UpdateRouteTableDetails()
            update_route_table_details.route_rules = route_rules
            network_client.update_route_table(default_route_table_ocid, update_route_table_details)

            network_client.delete_internet_gateway(ig_ocid)
            try:
                oci.wait_until(network_client, network_client.get_internet_gateway(ig_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except oci.exceptions.ServiceError as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)

            network_client.delete_vcn(vcn_ocid)

        except Exception as error:
            util.print_latest_exception(error)
            success_terminating_db_systems = False

        assert success_terminating_db_systems


def get_database(runner, config_file, config_profile, db_systems):
    """Returns the OCID of the first database listed in the db_system"""
    params = [
        'database', 'list',
        '--compartment-id', util.COMPARTMENT_ID,
        '--db-system-id', db_systems[0]
    ]
    params.extend(ADDITIONAL_PARAMETERS)
    result = invoke(runner, config_file, config_profile, params)
    print("get_database result.output", result.output)
    util.validate_response(result)

    json_result = json.loads(result.output)
    for db in json_result['data']:
        if db['lifecycle-state'] != 'TERMINATING' and db['lifecycle-state'] != 'TERMINATED':
            return db['id']


def create_subnet(cidr_block, subnet_dns_label, vcn_ocid, network_client, availability_domain=None):
    if availability_domain is None:
        availability_domain = util.availability_domain()
    # create subnet in first AD
    subnet_name = util.random_name('python_sdk_test_subnet')
    create_subnet_details = oci.core.models.CreateSubnetDetails()
    create_subnet_details.compartment_id = util.COMPARTMENT_ID
    create_subnet_details.availability_domain = availability_domain
    create_subnet_details.display_name = subnet_name
    create_subnet_details.vcn_id = vcn_ocid
    create_subnet_details.cidr_block = cidr_block
    create_subnet_details.dns_label = subnet_dns_label

    result = network_client.create_subnet(create_subnet_details)
    subnet_ocid = result.data.id
    assert result.status == 200
    oci.wait_until(network_client, network_client.get_subnet(subnet_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)
    return subnet_ocid


def random_db_name():
    random_name = util.random_name('clidb', insert_underscore=False)
    return random_name[-8:] if len(random_name) > 8 else random_name


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile', config_profile, 'db'] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + ['--config-file', config_file, '--profile', config_profile, 'db'] + params, ** args)

    return result
