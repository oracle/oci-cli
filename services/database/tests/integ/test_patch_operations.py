# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import pytest

from tests import util
from tests import test_config_container
from common_test_database import invoke, networking_cleanup, networking, db_systems, db_systems_cleanup, get_database, match_on
from common_test_database import CASSETTE_LIBRARY_DIR, DB_PATCH_TIME_SEC


@pytest.fixture(autouse=True, scope='module')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_patch_operations.yml'):
        yield


@pytest.fixture(scope='module')
def networking_test_patch_operations(runner, config_file, config_profile, network_client, request):
    subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client, "_patch_operations")
    yield networking_dict
    networking_cleanup(runner, config_file, config_profile, network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


@pytest.fixture(scope='module')
def db_systems_test_patch_operations(runner, config_file, config_profile, networking_test_patch_operations, network_client, request):
    db_system_id_1, db_system_id_2 = db_systems(runner, config_file, config_profile, networking_test_patch_operations, network_client, request)
    yield [db_system_id_1, db_system_id_2]
    db_systems_cleanup(runner, config_file, config_profile, db_system_id_1, db_system_id_2)


@pytest.fixture(scope='module')
def database_test_patch_operations(runner, config_file, config_profile, db_systems_test_patch_operations):
    return get_database(runner, config_file, config_profile, db_systems_test_patch_operations)


@util.long_running
def test_patch_operations(runner, config_file, config_profile, database_test_patch_operations, db_systems_test_patch_operations):
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
