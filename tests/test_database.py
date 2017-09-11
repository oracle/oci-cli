import json
import oci
import oci_cli
import pytest
import random

from . import util

ADMIN_PASSWORD = "BEstr0ng_#1"
DB_VERSION = '12.1.0.2'
DB_SYSTEM_PROVISIONING_TIME_SEC = 7200  # 2 hours

DB_PROVISIONING_TIME_SEC = 1200  # 20 minutes
DB_TERMINATING_TIME_SEC = 1200  # 20 minutes


@pytest.fixture(scope='module')
def subnet(network_client):
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

    subnet_name = util.random_name('python_sdk_test_subnet')
    cidr_block = "10.0.0.0/16"
    subnet_dns_label = util.random_name('subnet', insert_underscore=False)

    create_subnet_details = oci.core.models.CreateSubnetDetails()
    create_subnet_details.compartment_id = util.COMPARTMENT_ID
    create_subnet_details.availability_domain = util.availability_domain()
    create_subnet_details.display_name = subnet_name
    create_subnet_details.vcn_id = vcn_ocid
    create_subnet_details.cidr_block = cidr_block
    create_subnet_details.dns_label = subnet_dns_label

    result = network_client.create_subnet(create_subnet_details)
    subnet_ocid = result.data.id
    assert result.status == 200

    oci.wait_until(network_client, network_client.get_subnet(subnet_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

    yield subnet_ocid

    network_client.delete_subnet(subnet_ocid)

    try:
        oci.wait_until(network_client, network_client.get_subnet(subnet_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
    except oci.exceptions.ServiceError as error:
        if not hasattr(error, 'status') or error.status != 404:
            util.print_latest_exception(error)

    network_client.delete_vcn(vcn_ocid)


@pytest.fixture(scope='module')
def db_system(runner, config_file, config_profile, subnet):
    params = [
        'system', 'launch',
        '--admin-password', ADMIN_PASSWORD,
        '--availability-domain', util.availability_domain(),
        '--compartment-id', util.COMPARTMENT_ID,
        '--cpu-core-count', '4',
        '--database-edition', 'ENTERPRISE_EDITION',
        '--db-name', random_db_name(),
        '--db-version', DB_VERSION,
        '--display-name', util.random_name('CliDbSysDisplayName', insert_underscore=False),
        '--hostname', util.random_name('cli-test-hostname', insert_underscore=False),
        '--shape', 'BM.DenseIO1.36',
        '--ssh-authorized-keys-file', util.SSH_AUTHORIZED_KEYS_FILE,
        '--subnet-id', subnet
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    print(str(result.output))

    json_result = json.loads(result.output)
    db_system_id = json_result['data']['id']

    util.wait_until(['db', 'system', 'get', '--db-system-id', db_system_id], 'AVAILABLE', max_wait_seconds=DB_SYSTEM_PROVISIONING_TIME_SEC)

    yield db_system_id

    params = [
        'system', 'terminate',
        '--db-system-id', db_system_id,
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # validate that it goes into terminating state
    params = [
        'system', 'get',
        '--db-system-id', db_system_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    assert json.loads(result.output)['data']['lifecycle-state'] == "TERMINATING"


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
def test_update_db_system(runner, config_file, config_profile, db_system):
    params = [
        'system', 'update',
        '--cpu-core-count', '6',
        '--db-system-id', db_system,
        '--ssh-authorized-keys-file', util.SSH_AUTHORIZED_KEYS_FILE,
        '--force'  # disable confirm prompt for overwriting ssh keys list
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    util.wait_until(['db', 'system', 'get', '--db-system-id', db_system], 'AVAILABLE', max_wait_seconds=300)

    # db system has updated so verify new fields
    params = [
        'system', 'get',
        '--db-system-id', db_system
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    json_result = json.loads(result.output)
    assert json_result['data']['cpu-core-count'] == 6


@util.enable_long_running
def test_database_operations(runner, config_file, config_profile, db_system):
    # create database
    params = [
        'database', 'create',
        '--db-system-id', db_system,
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
        '--db-system-id', db_system
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # list databases with --limit 0
    params = [
        'database', 'list',
        '--compartment-id', util.COMPARTMENT_ID,
        '--db-system-id', db_system,
        '--limit', '0'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert len(result.output) == 0

    # delete database
    params = [
        'database', 'delete',
        '--database-id', database_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    util.wait_until(['db', 'database', 'get', '--database-id', database_id], 'TERMINATED', max_wait_seconds=DB_TERMINATING_TIME_SEC)


@util.enable_long_running
def test_db_node_operations(runner, config_file, config_profile, db_system):
    # list nodes in db-system
    params = [
        'node', 'list',
        '--compartment-id', util.COMPARTMENT_ID,
        '--db-system-id', db_system
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

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    assert json.loads(result.output)['data']['lifecycle-state'] == "STOPPING"

    # db node start
    params = [
        'node', 'start',
        '--db-node-id', node_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    assert json.loads(result.output)['data']['lifecycle-state'] == "STARTING"

    # db node reset
    params = [
        'node', 'reset',
        '--db-node-id', node_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    assert json.loads(result.output)['data']['lifecycle-state'] == "STOPPING"

    # db node start
    params = [
        'node', 'soft-reset',
        '--db-node-id', node_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    assert json.loads(result.output)['data']['lifecycle-state'] == "STOPPING"


def random_db_name():
    return 'clidb' + str(random.randint(0, 100))  # --db-name cannot be > 8 chars


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile', config_profile, 'db'] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + ['--config-file', config_file, '--profile', config_profile, 'db'] + params, ** args)

    return result
