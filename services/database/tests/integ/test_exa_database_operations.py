# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import pytest

from tests import util
from tests import test_config_container
from common_test_database import invoke, networking_cleanup, networking, exa_db_system, exa_db_system_cleanup, match_on
from common_test_database import CASSETTE_LIBRARY_DIR, ADMIN_PASSWORD, DB_VERSION, DB_RECOVERY_WINDOW
from common_test_database import DB_PROVISIONING_TIME_SEC, DB_TERMINATING_TIME_SEC


@pytest.fixture(autouse=True, scope='module')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_exa_database_operations.yml'):
        yield


@pytest.fixture(scope='module')
def networking_test_database_operations(runner, config_file, config_profile, network_client, request):
    subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client, "_exa_database_operations")
    yield networking_dict
    networking_cleanup(runner, config_file, config_profile, network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


@pytest.fixture(scope='module')
def exa_db_systems_test_database_operations(runner, config_file, config_profile, networking_test_database_operations, network_client, request):
    db_system_id_1 = exa_db_system(runner, config_file, config_profile, networking_test_database_operations, network_client, request)
    yield [db_system_id_1]
    exa_db_system_cleanup(runner, config_file, config_profile, db_system_id_1)


@util.long_running
def test_exa_database_operations(runner, config_file, config_profile, exa_db_systems_test_database_operations):

    # create database
    params = [
        'database', 'create',
        '--db-system-id', exa_db_systems_test_database_operations[0],
        '--db-version', DB_VERSION,
        '--admin-password', ADMIN_PASSWORD,
        '--db-name', 'clidbop4'
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
        '--db-system-id', exa_db_systems_test_database_operations[0]
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # list databases with --limit 0
    params = [
        'database', 'list',
        '--compartment-id', util.COMPARTMENT_ID,
        '--db-system-id', exa_db_systems_test_database_operations[0],
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
    util.wait_until(['db', 'system', 'get', '--db-system-id', exa_db_systems_test_database_operations[0]], 'AVAILABLE', max_wait_seconds=DB_TERMINATING_TIME_SEC)
