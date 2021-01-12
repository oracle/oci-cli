# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import pytest

from tests import util
from tests import test_config_container
from common_test_database import invoke, networking_cleanup, networking, db_systems, db_systems_cleanup, get_database, match_on
from common_test_database import CASSETTE_LIBRARY_DIR, ADMIN_PASSWORD, DB_SYSTEM_PROVISIONING_TIME_SEC, DB_TERMINATING_TIME_SEC
from common_test_database import DB_PROVISIONING_TIME_SEC, DB_SYSTEM_SHAPE, DB_BACKUP_TIME_SEC, DB_SYSTEM_DB_EXTREME_EDITION


@pytest.fixture(autouse=True, scope='module')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_backup_operations.yml'):
        yield


@pytest.fixture(scope='module')
def networking_test_backup_operations(runner, config_file, config_profile, network_client, request):
    subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client, "_backup_operations")
    yield networking_dict
    networking_cleanup(runner, config_file, config_profile, network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


@pytest.fixture(scope='module')
def db_systems_test_backup_operations(runner, config_file, config_profile, networking_test_backup_operations, network_client, request):
    db_system_id_1, db_system_id_2 = db_systems(runner, config_file, config_profile, networking_test_backup_operations, network_client, request)
    yield [db_system_id_1, db_system_id_2]
    db_systems_cleanup(runner, config_file, config_profile, db_system_id_1, db_system_id_2)


@pytest.fixture(scope='module')
def database_test_backup_operations(runner, config_file, config_profile, db_systems_test_backup_operations):
    return get_database(runner, config_file, config_profile, db_systems_test_backup_operations)


@util.long_running
@pytest.mark.skip("DEXREQ-698")
def test_backup_operations(runner, config_file, config_profile, db_systems_test_backup_operations, database_test_backup_operations):
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
    print(json.loads(result.output)['data'])
    subnet = json.loads(result.output)['data']['subnet-id']
    availbility_domain = json.loads(result.output)['data']['availability-domain']

    print("Launching new Dbsystem from backup with renamed database ")
    # Launch dbsystem
    params_1 = [
        'system', 'launch-from-backup',
        '--ssh-authorized-keys-file', util.SSH_AUTHORIZED_KEYS_FILE,
        '--backup-id', backup_id,
        '--subnet-id', subnet,
        '--hostname', util.random_name('cli-test-hostname', insert_underscore=False),
        '--db-name', 'renameDb',
        '--availability-domain', availbility_domain,
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
