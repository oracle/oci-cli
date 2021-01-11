# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import pytest

from tests import util
from tests import test_config_container
from common_test_database import invoke, networking_cleanup, networking, match_on
from common_test_database import CASSETTE_LIBRARY_DIR, ADMIN_PASSWORD, DB_SYSTEM_PROVISIONING_TIME_SEC, DB_VERSION
from common_test_database import DB_SYSTEM_CPU_CORE_COUNT, DB_SYSTEM_DB_EXTREME_EDITION, SKIP_CLEAN_UP_RESOURCES


@pytest.fixture(autouse=True, scope='module')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=match_on).use_cassette('database_test_launch_exa_db_system.yml'):
        yield


@pytest.fixture(scope='module')
def networking_test_launch_exa_db_system(runner, config_file, config_profile, network_client, request):
    subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid, networking_dict = networking(network_client, "_exa_db_system")
    subnet_response = network_client.get_subnet(subnet_ocid_1)
    networking_dict['availability_domain'] = subnet_response.data.availability_domain
    yield networking_dict
    networking_cleanup(runner, config_file, config_profile, network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid)


def test_launch_exa_db_system(runner, config_file, config_profile, networking_test_launch_exa_db_system):
    DB_SYSTEM_SHAPE = 'Exadata.Quarter2.92'

    # provision DB systems
    params = [
        'system', 'launch',
        '--admin-password', ADMIN_PASSWORD,
        '--availability-domain', networking_test_launch_exa_db_system['availability_domain'],
        '--compartment-id', util.COMPARTMENT_ID,
        '--cpu-core-count', DB_SYSTEM_CPU_CORE_COUNT,
        '--database-edition', DB_SYSTEM_DB_EXTREME_EDITION,
        '--time-zone', 'US/Pacific',
        '--db-name', 'clidbexa',
        '--db-version', DB_VERSION,
        '--display-name', 'CliDbSysExa',
        '--hostname', 'cliexa',
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
