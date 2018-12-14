# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import json
import oci
import oci_cli
import os
import pytest

from . import util
from . import test_config_container

ADMIN_PASSWORD = "BEstr0ng_#1"
DB_VERSION = '12.1.0.2'
DB_SYSTEM_CPU_CORE_COUNT = '4'
DB_SYSTEM_DB_EDITION = 'ENTERPRISE_EDITION'
DB_SYSTEM_DB_EXTREME_EDITION = 'ENTERPRISE_EDITION_EXTREME_PERFORMANCE'
DB_SYSTEM_SHAPE = 'BM.DenseIO1.36'
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

# by default clean up all resources. if OCI_CLI_SKIP_CLEAN_UP_DB_RESOURCES == '1' then do not clean up resources
SKIP_CLEAN_UP_RESOURCES = os.environ.get('OCI_CLI_SKIP_CLEAN_UP_DB_RESOURCES') == '1'


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    # We are doing this b/c we have recent recordings with data for test_data_guard_with_new_db
    # from our new tenancy, but still have old recordings and for the other tests.
    # Unfortunately, at this time we don't have the proper limits to re-record the old tests.
    if request.function.__name__ in ["test_data_guard_with_new_db", "test_launch_exa_db_system", "test_launch_db_from_database"]:
        match_on = ['method', 'scheme', 'host', 'port']
    else:
        match_on = []
    my_vcr = test_config_container.create_vcr(match_on=match_on).use_cassette('database_{name}.yml'.format(name=request.function.__name__))
    with my_vcr:
        yield


@pytest.fixture(autouse=True, scope='function')
def log_test(request):
    print("Test {name}...".format(name=request.function.__name__))
    yield
    print("Test {name} Complete".format(name=request.function.__name__))


@pytest.fixture(scope='module')
def networking(runner, config_file, config_profile, network_client, request):
    # create VCN
    vcn_name = util.random_name('cli_db_test_vcn')
    cidr_block = "10.0.0.0/16"
    vcn_dns_label = util.random_name('vcn', insert_underscore=False)

    create_vcn_details = oci.core.models.CreateVcnDetails()
    create_vcn_details.cidr_block = cidr_block
    create_vcn_details.display_name = vcn_name
    create_vcn_details.compartment_id = util.COMPARTMENT_ID
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
    yield networking_dict

    # this code does not run inside the vcr_fixture because it is outside any test function
    # thus we are explicitly creating a separate cassette for it here
    with test_config_container.create_vcr().use_cassette('database_test_cleanup.yml'):
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

            network_client.delete_vcn(vcn_ocid)

        except Exception as error:
            util.print_latest_exception(error)
            success_terminating_db_systems = False

        assert success_terminating_db_systems


@pytest.fixture(scope='module')
def db_systems(runner, config_file, config_profile, networking, request):
    # allow running against existing DB systems instead of launching new ones to save time
    if EXISTING_DB_SYSTEM_1 and EXISTING_DB_SYSTEM_2:
        yield [EXISTING_DB_SYSTEM_1, EXISTING_DB_SYSTEM_2]
        return

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

    params = [
        'system', 'launch',
        '--admin-password', ADMIN_PASSWORD,
        '--availability-domain', util.second_availability_domain(),
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
        '--initial-data-storage-size-in-gb', '256'
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
    yield [db_system_id_1, db_system_id_2]

    # this code does not run inside the vcr_fixture because it is outside any test function
    # thus we are explicitly creating a separate cassette for it here
    with test_config_container.create_vcr().use_cassette('database_test_cleanup.yml'):
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

            assert json.loads(result.output)['data']['lifecycle-state'] == "TERMINATING"
            util.wait_until(['db', 'system', 'get', '--db-system-id', db_system_id_1], 'TERMINATED', max_wait_seconds=DB_SYSTEM_PROVISIONING_TIME_SEC, succeed_if_not_found=True)
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

            assert json.loads(result.output)['data']['lifecycle-state'] == "TERMINATING"
            util.wait_until(['db', 'system', 'get', '--db-system-id', db_system_id_2], 'TERMINATED', max_wait_seconds=DB_SYSTEM_PROVISIONING_TIME_SEC, succeed_if_not_found=True)
        except Exception as error:
            util.print_latest_exception(error)
            success_terminating_db_systems = False

        assert success_terminating_db_systems


@pytest.fixture(scope='module')
def vm_db_system(runner, config_file, config_profile, networking, request):
    DB_SYSTEM_SHAPE = 'VM.Standard2.1'
    if EXISTING_VM_DB_SYSTEM:
        yield [EXISTING_VM_DB_SYSTEM]
        return

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
    print("DB System provisioned successfully!")
    yield [db_system_id_1]

    # this code does not run inside the vcr_fixture because it is outside any test function
    # thus we are explicitly creating a separate cassette for it here
    with test_config_container.create_vcr().use_cassette('database_test_cleanup.yml'):
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

            assert json.loads(result.output)['data']['lifecycle-state'] == "TERMINATING"
            util.wait_until(['db', 'system', 'get', '--db-system-id', db_system_id_1], 'TERMINATED', max_wait_seconds=DB_SYSTEM_PROVISIONING_TIME_SEC, succeed_if_not_found=True)
        except Exception as error:
            util.print_latest_exception(error)
            success_terminating_db_systems = False

        assert success_terminating_db_systems


@pytest.fixture(scope='function')
def database(runner, config_file, config_profile, db_systems):
    return get_database(runner, config_file, config_profile, db_systems)


@pytest.fixture(scope='function')
def vm_database(runner, config_file, config_profile, vm_db_system):
    return get_database(runner, config_file, config_profile, vm_db_system)


def get_database(runner, config_file, config_profile, db_systems):
    """Returns the OCID of the first database listed in the db_system"""

    params = [
        'database', 'list',
        '--compartment-id', util.COMPARTMENT_ID,
        '--db-system-id', db_systems[0]
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    json_result = json.loads(result.output)
    for db in json_result['data']:
        if db['lifecycle-state'] != 'TERMINATING' and db['lifecycle-state'] != 'TERMINATED':
            return db['id']


def test_list_db_systems(runner, config_file, config_profile):
    # other db system operations are covered by the db_system fixture (create, get, delete)
    params = [
        'system', 'list',
        '--compartment-id', util.COMPARTMENT_ID
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


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


def test_list_db_versions(runner, config_file, config_profile):
    params = [
        'version', 'list',
        '--compartment-id', util.COMPARTMENT_ID
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # validate that we get back multiple versions
    assert len(json.loads(result.output)['data']) > 0


@util.long_running
def test_update_db_system(runner, config_file, config_profile, db_systems):

    params = [
        'system', 'update',
        '--db-system-id', db_systems[0],
        '--cpu-core-count', '6',
        '--ssh-authorized-keys-file', util.SSH_AUTHORIZED_KEYS_FILE,
        '--force'  # disable confirm prompt for overwriting ssh keys list
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    util.wait_until(['db', 'system', 'get', '--db-system-id', db_systems[0]], 'AVAILABLE', max_wait_seconds=DB_SYSTEM_UPDATE_TIME)

    # db system has updated so verify new fields
    params = [
        'system', 'get',
        '--db-system-id', db_systems[0]
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    json_result = json.loads(result.output)
    assert json_result['data']['cpu-core-count'] == 6

    print("Updated DB System: " + result.output)


###########################
# DATA GUARD OPERATIONS
###########################
@util.long_running
def test_data_guard_operations(runner, config_file, config_profile, database, db_systems):
    # verify db system 1 is available
    params = [
        'system', 'get',
        '--db-system-id', db_systems[0]
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    db_system_1_state = json.loads(result.output)['data']['lifecycle-state']

    # verify db system 2 is available
    params = [
        'system', 'get',
        '--db-system-id', db_systems[1]
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    db_system_2_state = json.loads(result.output)['data']['lifecycle-state']

    if db_system_1_state != "AVAILABLE":
        print("Waiting for DB system 1 to become AVAILABLE")
        util.wait_until(['db', 'system', 'get', '--db-system-id', db_systems[0]], 'AVAILABLE', max_wait_seconds=300)

    if db_system_2_state != "AVAILABLE":
        print("Waiting for DB system 2 to become AVAILABLE")
        util.wait_until(['db', 'system', 'get', '--db-system-id', db_systems[1]], 'AVAILABLE', max_wait_seconds=300)

    # CREATE
    # data guard requires 2 distinct DB systems
    # 'database' comes from db_systems[0] and db_systems[1] is used as the peer db system
    print("Creating Data Guard Association...")
    params = [
        'data-guard-association', 'create', 'from-existing-db-system',
        '--database-id', database,
        '--creation-type', 'ExistingDbSystem',
        '--database-admin-password', ADMIN_PASSWORD,
        '--protection-mode', 'MAXIMUM_PERFORMANCE',
        '--transport-type', 'ASYNC',
        '--peer-db-system-id', db_systems[1]
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    data_guard_association_id = json.loads(result.output)['data']['id']

    util.wait_until(['db', 'data-guard-association', 'get', '--database-id', database, '--data-guard-association-id', data_guard_association_id], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)

    util.wait_until(['db', 'system', 'get', '--db-system-id', db_systems[0]], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
    util.wait_until(['db', 'system', 'get', '--db-system-id', db_systems[1]], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)

    # LIST
    params = [
        'data-guard-association', 'list',
        '--database-id', database
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    assert len(json.loads(result.output)['data']) > 0

    # GET
    params = [
        'data-guard-association', 'get',
        '--database-id', database,
        '--data-guard-association-id', data_guard_association_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    peer_database_id = json.loads(result.output)['data']['peer-database-id']
    peer_data_guard_association_id = json.loads(result.output)['data']['peer-data-guard-association-id']

    # ensure both databases are available
    util.wait_until(['db', 'database', 'get', '--database-id', database], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
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
    util.wait_until(['db', 'database', 'get', '--database-id', database], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
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

    util.wait_until(['db', 'database', 'get', '--database-id', database], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
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

    util.wait_until(['db', 'database', 'get', '--database-id', database], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
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


@util.long_running
def test_data_guard_with_new_db(runner, config_file, config_profile, vm_database, vm_db_system):
    # Get the subnet of the existing database
    params = ['system', 'get', '--db-system-id', vm_db_system[0]]
    result = invoke(runner, config_file, config_profile, params)
    subnet_id = json.loads(result.output)['data']['subnet-id']

    # CREATE using a new DB rather than an existing one.
    # 'database' comes from vm_db_system[0] and the second one will be created.
    print("Creating Data Guard Association...")
    params = [
        'data-guard-association', 'create', 'with-new-db-system',
        '--database-id', vm_database,
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
    util.wait_until(['db', 'data-guard-association', 'get', '--database-id', vm_database, '--data-guard-association-id', data_guard_association_id], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
    util.wait_until(['db', 'system', 'get', '--db-system-id', vm_db_system[0]], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)

    # LIST
    params = [
        'data-guard-association', 'list',
        '--database-id', vm_database
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert len(json.loads(result.output)['data']) > 0

    # GET
    params = [
        'data-guard-association', 'get',
        '--database-id', vm_database,
        '--data-guard-association-id', data_guard_association_id
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    peer_database_id = json.loads(result.output)['data']['peer-database-id']
    peer_db_system_id = json.loads(result.output)['data']['peer-db-system-id']
    peer_data_guard_association_id = json.loads(result.output)['data']['peer-data-guard-association-id']
    # ensure both databases are available
    util.wait_until(['db', 'database', 'get', '--database-id', vm_database], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
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
    util.wait_until(['db', 'database', 'get', '--database-id', vm_database], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
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
    util.wait_until(['db', 'database', 'get', '--database-id', vm_database], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
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
    util.wait_until(['db', 'database', 'get', '--database-id', vm_database], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)
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
    assert json.loads(result.output)['data']['lifecycle-state'] == "TERMINATING"
    util.wait_until(['db', 'system', 'get', '--db-system-id', peer_db_system_id], 'TERMINATED', max_wait_seconds=DB_SYSTEM_PROVISIONING_TIME_SEC, succeed_if_not_found=True)
    util.wait_until(['db', 'system', 'get', '--db-system-id', vm_db_system[0]], 'AVAILABLE', max_wait_seconds=DATA_GUARD_ASSOCIATION_OPERATION_TIME)

    # LIST
    params = [
        'data-guard-association', 'list',
        '--database-id', vm_database
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert len(json.loads(result.output)['data']) > 0


@util.long_running
def test_database_operations(runner, config_file, config_profile, db_systems):
    # create database
    params = [
        'database', 'create',
        '--db-system-id', db_systems[0],
        '--db-version', DB_VERSION,
        '--admin-password', ADMIN_PASSWORD,
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
        '--db-system-id', db_systems[0]
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # list databases with --limit 0
    params = [
        'database', 'list',
        '--compartment-id', util.COMPARTMENT_ID,
        '--db-system-id', db_systems[0],
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
    util.wait_until(['db', 'system', 'get', '--db-system-id', db_systems[0]], 'AVAILABLE', max_wait_seconds=DB_TERMINATING_TIME_SEC)


@util.long_running
def test_backup_operations(runner, config_file, config_profile, db_systems, database):
    # create backup
    params = [
        'backup', 'create',
        '--database-id', database,
        '--display-name', util.random_name('CliDbBackup')
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    json_result = json.loads(result.output)
    backup_id = json_result['data']['id']

    # get backup
    util.wait_until(['db', 'backup', 'get', '--backup-id', backup_id], 'ACTIVE', max_wait_seconds=DB_BACKUP_TIME_SEC)

    # list backups by database
    params = [
        'backup', 'list',
        '--database-id', database
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
        '--database-id', database,
        '--latest', 'true'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    util.wait_until(['db', 'database', 'get', '--database-id', database], 'AVAILABLE', max_wait_seconds=DB_BACKUP_TIME_SEC)

    # in order to create from backup we have to delete this database
    print("Deleting database in order to create from backup...")
    params = [
        'database', 'delete',
        '--database-id', database,
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    util.wait_until(['db', 'database', 'get', '--database-id', database], 'TERMINATED', max_wait_seconds=DB_TERMINATING_TIME_SEC, succeed_if_not_found=True)
    util.wait_until(['db', 'system', 'get', '--db-system-id', db_systems[0]], 'AVAILABLE', max_wait_seconds=DB_TERMINATING_TIME_SEC)

    # create from backup
    params = [
        'database', 'create-from-backup',
        '--db-system-id', db_systems[0],
        '--backup-id', backup_id,
        '--admin-password', ADMIN_PASSWORD,
        '--backup-tde-password', ADMIN_PASSWORD
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    db_created_from_backup = json.loads(result.output)['data']['id']

    util.wait_until(['db', 'database', 'get', '--database-id', db_created_from_backup], 'AVAILABLE', max_wait_seconds=DB_PROVISIONING_TIME_SEC)

    # delete backup
    params = [
        'backup', 'delete',
        '--backup-id', backup_id,
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    util.wait_until(['db', 'backup', 'get', '--backup-id', backup_id], 'TERMINATED', max_wait_seconds=DB_PROVISIONING_TIME_SEC, succeed_if_not_found=True)


@util.long_running
def test_db_node_operations(runner, config_file, config_profile, db_systems):
    # list nodes in db-system
    params = [
        'node', 'list',
        '--compartment-id', util.COMPARTMENT_ID,
        '--db-system-id', db_systems[0]
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

    util.wait_until(['db', 'system', 'get', '--db-system-id', db_systems[0]], 'AVAILABLE', max_wait_seconds=DB_NODE_OPERATION_TIME)


###########################
# PATCH OPERATIONS
###########################
@util.long_running
def test_patch_operations(runner, config_file, config_profile, database, db_systems):
    # by db-system
    params = [
        'patch', 'list', 'by-db-system',
        '--db-system-id', db_systems[0]
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    if len(result.output) > 0:
        json_result = json.loads(result.output)
        if len(json_result['data']) > 0:
            patch_id = json_result['data'][0]['id']
            print("Getting patch {} for db system {}".format(patch_id, db_systems[0]))

            params = [
                'patch', 'get', 'by-db-system',
                '--db-system-id', db_systems[0],
                '--patch-id', patch_id
            ]

            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result)

            json_result = json.loads(result.output)
            if 'APPLY' in json_result['data']['available-actions']:
                print('Applying patch: {} to db system: {}'.format(patch_id, db_systems[0]))

                params = [
                    'db-system', 'patch',
                    '--db-system-id', db_systems[0],
                    '--patch-id', patch_id,
                    '--patch-action', 'APPLY'
                ]

                result = invoke(runner, config_file, config_profile, params)
                util.validate_response(result)

                util.wait_until(['db', 'system', 'get', '--db-system-id', db_systems[0]], 'AVAILABLE', max_wait_seconds=DB_PATCH_TIME_SEC)

    # by database
    params = [
        'patch', 'list', 'by-database',
        '--database-id', database
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    if len(result.output) > 0:
        json_result = json.loads(result.output)
        if len(json_result['data']) > 0:
            patch_id = json_result['data'][0]['id']
            print("Getting patch {} for database {}".format(patch_id, database))

            params = [
                'patch', 'get', 'by-database',
                '--database-id', database,
                '--patch-id', patch_id
            ]

            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result)

            json_result = json.loads(result.output)
            if 'APPLY' in json_result['data']['available-actions']:
                print('Applying patch: {} to database: {}'.format(patch_id, database))

                params = [
                    'database', 'patch',
                    '--database-id', database,
                    '--patch-id', patch_id,
                    '--patch-action', 'APPLY'
                ]

                result = invoke(runner, config_file, config_profile, params)
                util.validate_response(result)

                util.wait_until(['db', 'database', 'get', '--database-id', database], 'AVAILABLE', max_wait_seconds=DB_PATCH_TIME_SEC)


###########################
# PATCH HISTORY OPERATIONS
###########################
@util.long_running
def test_patch_history_operations(runner, config_file, config_profile, database, db_systems):
    # by db-system
    params = [
        'patch-history', 'list', 'by-db-system',
        '--db-system-id', db_systems[0]
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    if len(result.output) > 0:
        json_result = json.loads(result.output)
        if len(json_result['data']) > 0:
            patch_history_entry_id = json_result['data'][0]['id']

            params = [
                'patch-history', 'get', 'by-db-system',
                '--db-system-id', db_systems[0],
                '--patch-history-entry-id', patch_history_entry_id
            ]

            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result)

    # by database
    params = [
        'patch-history', 'list', 'by-database',
        '--database-id', database
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    if len(result.output) > 0:
        json_result = json.loads(result.output)
        if len(json_result['data']) > 0:
            patch_history_entry_id = json_result['data'][0]['id']

            params = [
                'patch-history', 'get', 'by-database',
                '--database-id', database,
                '--patch-history-entry-id', patch_history_entry_id
            ]

            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result)


def create_subnet(cidr_block, subnet_dns_label, vcn_ocid, network_client, availability_domain=util.availability_domain()):
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


def test_launch_exa_db_system(runner, config_file, config_profile, networking):
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
        '--display-name', util.random_name('CliDbSysDisplayName', insert_underscore=False),
        '--hostname', util.random_name('cli-test-hostname', insert_underscore=False),
        '--shape', DB_SYSTEM_SHAPE,
        '--ssh-authorized-keys-file', util.SSH_AUTHORIZED_KEYS_FILE,
        '--subnet-id', networking['subnet_ocid_1'],
        '--backup-subnet-id', networking['subnet_ocid_2'],
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
