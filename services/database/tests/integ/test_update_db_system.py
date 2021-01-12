# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import pytest

from tests import util
from tests import test_config_container
from common_test_database import invoke, networking_cleanup, networking, db_systems, db_systems_cleanup, match_on
from common_test_database import CASSETTE_LIBRARY_DIR, DB_SYSTEM_UPDATE_TIME


@pytest.fixture(autouse=True, scope='module')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_update_db_system.yml'):
        yield


@pytest.fixture(scope='module')
def networking_test_update_db_system(runner, config_file, config_profile, network_client, request):
    subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client, "_test_update_db_system")
    yield networking_dict
    networking_cleanup(runner, config_file, config_profile, network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


@pytest.fixture(scope='module')
def db_systems_test_update_db_system(runner, config_file, config_profile, networking_test_update_db_system, network_client, request):
    db_system_id_1, db_system_id_2 = db_systems(runner, config_file, config_profile, networking_test_update_db_system, network_client, request)
    yield [db_system_id_1, db_system_id_2]
    db_systems_cleanup(runner, config_file, config_profile, db_system_id_1, db_system_id_2)


@util.long_running
def test_update_db_system(runner, config_file, config_profile, db_systems_test_update_db_system):
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
