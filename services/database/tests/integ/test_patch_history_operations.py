# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import pytest

from tests import util
from tests import test_config_container
from common_test_database import invoke, networking_cleanup, networking, db_systems, db_systems_cleanup, get_database, match_on
from common_test_database import CASSETTE_LIBRARY_DIR


@pytest.fixture(autouse=True, scope='module')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_patch_history_operations.yml'):
        yield


@pytest.fixture(scope='module')
def networking_test_patch_history_operations(runner, config_file, config_profile, network_client, request):
    subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client, "_patch_history_operations")
    yield networking_dict
    networking_cleanup(runner, config_file, config_profile, network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


@pytest.fixture(scope='module')
def db_systems_test_patch_history_operations(runner, config_file, config_profile, networking_test_patch_history_operations, network_client, request):
    db_system_id_1, db_system_id_2 = db_systems(runner, config_file, config_profile, networking_test_patch_history_operations, network_client, request)
    yield [db_system_id_1, db_system_id_2]
    db_systems_cleanup(runner, config_file, config_profile, db_system_id_1, db_system_id_2)


@pytest.fixture(scope='module')
def database_test_patch_history_operations(runner, config_file, config_profile, db_systems_test_patch_history_operations):
    return get_database(runner, config_file, config_profile, db_systems_test_patch_history_operations)


@util.long_running
def test_patch_history_operations(runner, config_file, config_profile, database_test_patch_history_operations, db_systems_test_patch_history_operations):
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
