# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

'''
# After setting your test environment for CLI,
# These tests work collectively, this way:
# export CLI_TESTS_ADMIN_PASS_PHRASE="XXXXXXXX"
# pytest -s --enable-long-running --vcr-record-mode=none services/database/tests/integ
'''

import json
import oci_cli
import oci
import os
import pytest
from tests import util

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


# Used by test_create_db_from_db.py, test_launch_db_from_db.py
def bm_db_system(runner, config_file, config_profile, networking, network_client, request):
    DB_SYSTEM_SHAPE = "BM.DenseIO2.52"
    if EXISTING_DB_SYSTEM_1:
        return [EXISTING_DB_SYSTEM_1]
    else:
        subnet_response = network_client.get_subnet(networking['subnet_ocid_1'])
        print("Using subnet's AD", subnet_response.data.availability_domain)
        # provision DB systems
        params = [
            'system', 'launch',
            '--admin-password', ADMIN_PASSWORD,
            '--availability-domain', subnet_response.data.availability_domain,
            '--compartment-id', util.COMPARTMENT_ID,
            '--cpu-core-count', DB_SYSTEM_CPU_CORE_COUNT,
            '--database-edition', DB_SYSTEM_DB_EDITION,
            '--db-name', 'clibmdb',
            '--db-version', DB_VERSION,
            '--display-name', 'CliDbSysDisplayNameBm',
            '--hostname', 'cli-bm-host',
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


# test_data_guard_with_new_db.py
def vm_db_system(runner, config_file, config_profile, networking, network_client, request):
    DB_SYSTEM_SHAPE = 'VM.Standard2.1'
    if EXISTING_VM_DB_SYSTEM:
        return [EXISTING_VM_DB_SYSTEM, ]
    else:
        subnet_response = network_client.get_subnet(networking['subnet_ocid_1'])
        print("Using subnet's AD", subnet_response.data.availability_domain)
        # provision DB systems
        params = [
            'system', 'launch',
            '--admin-password', ADMIN_PASSWORD,
            '--availability-domain', subnet_response.data.availability_domain,
            '--compartment-id', util.COMPARTMENT_ID,
            '--cpu-core-count', DB_SYSTEM_CPU_CORE_COUNT,
            '--database-edition', DB_SYSTEM_DB_EDITION,
            '--db-name', 'clivmdb',
            '--db-version', DB_VERSION,
            '--display-name', 'CliDbSysDisplayNameVm',
            '--hostname', 'cli-vm-hostname',
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


# Used by test_backup_operations.py, test_data_guard_operations.py, test_database_operations.py
# test_db_node_operations.py, test_patch_history_operations.py, test_patch_operations.py,
# test_update_db_system.py.
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
            '--db-name', 'clidb1',
            '--db-version', DB_VERSION,
            '--display-name', 'CliDbSysDisplayName1',
            '--hostname', 'cli-host1',
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
            '--db-name', 'clidb2',
            '--db-version', DB_VERSION,
            '--display-name', 'CliDbSysDisplayName2',
            '--hostname', 'cli-host2',
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


def exa_db_system(runner, config_file, config_profile, networking, network_client, request):
    DB_SYSTEM_SHAPE = "Exadata.Quarter1.84"
    DB_SYSTEM_CPU_CORE_COUNT = '22'
    if EXISTING_DB_SYSTEM_1:
        return [EXISTING_DB_SYSTEM_1]
    else:
        subnet_response = network_client.get_subnet(networking['subnet_ocid_1'])
        print("Using subnet's AD", subnet_response.data.availability_domain)
        # provision DB systems
        params = [
            'system', 'launch',
            '--admin-password', ADMIN_PASSWORD,
            '--availability-domain', subnet_response.data.availability_domain,
            '--compartment-id', util.COMPARTMENT_ID,
            '--cpu-core-count', DB_SYSTEM_CPU_CORE_COUNT,
            '--database-edition', DB_SYSTEM_DB_EXTREME_EDITION,
            '--db-name', 'clibmdb',
            '--db-version', DB_VERSION,
            '--display-name', 'CliDbSysDisplayNameExa',
            '--hostname', 'cli-bm-host',
            '--shape', DB_SYSTEM_SHAPE,
            '--ssh-authorized-keys-file', util.SSH_AUTHORIZED_KEYS_FILE,
            '--subnet-id', networking['subnet_ocid_1'],
            '--backup-subnet-id', networking['subnet_ocid_2'],
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
        print("exa_db_system: DB System provisioned successfully!")
        return db_system_id_1


def exa_db_system_cleanup(runner, config_file, config_profile, db_system_id_1):
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


def networking(network_client, suffix):
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
        vcn_name = 'cli_db_test_vcn' + suffix
        cidr_block = "10.0.0.0/16"
        vcn_dns_label = 'vcnDns'

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
        subnet_dns_label = 'subnet1Dns'
        subnet_ocid_1 = create_subnet("10.0.1.0/24", subnet_dns_label, vcn_ocid, network_client, suffix)

        # create subnet in second AD
        subnet_dns_label = 'subnet2Dns'
        subnet_ocid_2 = create_subnet("10.0.0.0/24", subnet_dns_label, vcn_ocid, network_client, suffix)

        # open up security list to allow data guard operations
        response = network_client.list_security_lists(util.COMPARTMENT_ID, vcn_id=vcn_ocid)

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
        # create_ig_details.display_name = util.random_name('cli_db_ig')
        create_ig_details.display_name = 'cli_db_ig' + suffix
        create_ig_details.vcn_id = vcn_ocid

        response = network_client.create_internet_gateway(create_ig_details)
        ig_ocid = response.data.id

        # add rule targeting internet gateway to default route table (first and only route table in list)
        response = network_client.list_route_tables(util.COMPARTMENT_ID, vcn_id=vcn_ocid)
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


def networking_cleanup(runner, config_file, config_profile, network_client, subnet_ocid_1, subnet_ocid_2, default_route_table_ocid, ig_ocid, vcn_ocid):
    if SKIP_CLEAN_UP_RESOURCES:
        print("Skipping clean up of DB systems and dependent resources.")
        return

    success_terminating_db_systems = True
    try:
        # delete VCN and subnets now that dependent DB systems are deleted
        subnet_params = ["subnet", "delete", "--force", "--subnet-id", subnet_ocid_1, "--wait-for-state", "TERMINATED"]
        invoke(runner, config_file, config_profile, subnet_params)
        try:
            runner.invoke(oci_cli.cli, ['--config-file', config_file, '--profile', config_profile, 'network'] + subnet_params)
        except oci.exceptions.ServiceError as error:
            if not hasattr(error, 'status') or error.status != 404:
                util.print_latest_exception(error)

        subnet_params = ["subnet", "delete", "--force", "--subnet-id", subnet_ocid_2, "--wait-for-state", "TERMINATED"]
        invoke(runner, config_file, config_profile, subnet_params)
        try:
            runner.invoke(oci_cli.cli, ['--config-file', config_file, '--profile', config_profile, 'network'] + subnet_params)
        except oci.exceptions.ServiceError as error:
            if not hasattr(error, 'status') or error.status != 404:
                util.print_latest_exception(error)

        route_table_params = ["route-table", "--force", "--rt-id", default_route_table_ocid, "--route-rules", "'[]'", ]
        runner.invoke(oci_cli.cli, ['--config-file', config_file, '--profile', config_profile, 'network'] + route_table_params)

        try:
            ig_params = ['internet-gateway', 'delete', '--force', '--ig-id', ig_ocid, '--wait-for-state', 'TERMINATED']
            runner.invoke(oci_cli.cli, ['--config-file', config_file, '--profile', config_profile, 'network'] + ig_params)
        except oci.exceptions.ServiceError as error:
            if not hasattr(error, 'status') or error.status != 404:
                util.print_latest_exception(error)

        vcn_params = ['delete', '--vcn-id', vcn_ocid]
        runner.invoke(oci_cli.cli, ['--config-file', config_file, '--profile', config_profile, 'network'] + vcn_params)

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


def create_subnet(cidr_block, subnet_dns_label, vcn_ocid, network_client, suffix, availability_domain=None):
    if availability_domain is None:
        availability_domain = util.retrieve_availability_domains()[0]
    # create subnet in first AD
    subnet_name = 'python_sdk_test_subnet' + suffix
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
