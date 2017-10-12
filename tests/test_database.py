import json
import oci
import oci_cli
import pytest
import random

from . import util

ADMIN_PASSWORD = "BEstr0ng_#1"
DB_VERSION = '12.1.0.2'
DB_SYSTEM_CPU_CORE_COUNT = '4'
DB_SYSTEM_DB_EDITION = 'ENTERPRISE_EDITION'
DB_SYSTEM_SHAPE = 'BM.DenseIO1.36'
DB_SYSTEM_PROVISIONING_TIME_SEC = 14400  # 4 hours
DB_SYSTEM_UPDATE_TIME = 1800  # 30 minutes

DB_PROVISIONING_TIME_SEC = 1800  # 30 minutes
DB_TERMINATING_TIME_SEC = 1800  # 30 minutes

DATA_GUARD_ASSOCIATION_OPERATION_TIME = 1800  # 30 minutes
DB_NODE_OPERATION_TIME = 1800  # 30 minutes


@pytest.fixture(autouse=True, scope='function')
def log_test(request):
    print("Test {name}...".format(name=request.function.__name__))
    yield
    print("Test {name} Complete".format(name=request.function.__name__))


@pytest.fixture(scope='module')
def subnets(network_client):
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
    subnet_name = util.random_name('python_sdk_test_subnet')
    cidr_block = "10.0.1.0/24"
    subnet_dns_label = util.random_name('subnet', insert_underscore=False)

    create_subnet_details = oci.core.models.CreateSubnetDetails()
    create_subnet_details.compartment_id = util.COMPARTMENT_ID
    create_subnet_details.availability_domain = util.availability_domain()
    create_subnet_details.display_name = subnet_name
    create_subnet_details.vcn_id = vcn_ocid
    create_subnet_details.cidr_block = cidr_block
    create_subnet_details.dns_label = subnet_dns_label

    result = network_client.create_subnet(create_subnet_details)
    subnet_ocid_1 = result.data.id
    assert result.status == 200

    oci.wait_until(network_client, network_client.get_subnet(subnet_ocid_1), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

    # create subnet in second AD
    subnet_name = util.random_name('python_sdk_test_subnet')
    cidr_block = "10.0.0.0/24"
    subnet_dns_label = util.random_name('subnet', insert_underscore=False)

    create_subnet_details = oci.core.models.CreateSubnetDetails()
    create_subnet_details.compartment_id = util.COMPARTMENT_ID
    create_subnet_details.availability_domain = util.second_availability_domain()
    create_subnet_details.display_name = subnet_name
    create_subnet_details.vcn_id = vcn_ocid
    create_subnet_details.cidr_block = cidr_block
    create_subnet_details.dns_label = subnet_dns_label

    result = network_client.create_subnet(create_subnet_details)
    subnet_ocid_2 = result.data.id
    assert result.status == 200

    oci.wait_until(network_client, network_client.get_subnet(subnet_ocid_2), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

    # open up security list to allow data guard operations
    response = network_client.list_security_lists(util.COMPARTMENT_ID, vcn_ocid)

    # we just created this VCN so assume there is only one security list and it is the default
    default_security_list = response.data[0]

    # add new permissive ingress security rule
    new_allow_all_rule = oci.core.models.IngressSecurityRule()
    new_allow_all_rule.is_stateless = False
    new_allow_all_rule.protocol = "all"
    new_allow_all_rule.source = "0.0.0.0/0"

    default_security_list.ingress_security_rules.append(new_allow_all_rule)

    update_security_list_details = oci.core.models.UpdateSecurityListDetails()
    update_security_list_details.egress_security_rules = default_security_list.egress_security_rules
    update_security_list_details.ingress_security_rules = default_security_list.ingress_security_rules

    network_client.update_security_list(default_security_list.id, update_security_list_details)

    yield [subnet_ocid_1, subnet_ocid_2]

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


@pytest.fixture(scope='module')
def db_systems(runner, config_file, config_profile, subnets):
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
        '--subnet-id', subnets[0],
        '--license-model', 'LICENSE_INCLUDED'
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
        '--subnet-id', subnets[1],
        '--license-model', 'LICENSE_INCLUDED'
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
    except Exception as error:
        util.print_latest_exception(error)
        success_terminating_db_systems = False

    assert success_terminating_db_systems


@pytest.fixture(scope='module')
def database(runner, config_file, config_profile, db_systems):
    """Returns the OCID of the first database listed in the db_system"""

    params = [
        'database', 'list',
        '--compartment-id', util.COMPARTMENT_ID,
        '--db-system-id', db_systems[0]
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    json_result = json.loads(result.output)
    return json_result['data'][0]['id']


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


@util.enable_long_running
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


@util.enable_long_running
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


###########################
# DATA GUARD OPERATIONS
###########################
@util.enable_long_running
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


@util.enable_long_running
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


def random_db_name():
    return 'clidb' + str(random.randint(0, 100))  # --db-name cannot be > 8 chars


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile', config_profile, 'db'] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + ['--config-file', config_file, '--profile', config_profile, 'db'] + params, ** args)

    return result
