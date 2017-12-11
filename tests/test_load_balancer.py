# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import datetime
import json
import oci
import oci_cli
from oci_cli import cli_util
import os
import pytest
from . import util

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes

LB_PROVISIONING_TIME_SEC = 300  # 5 minutes
LB_PRIVATE_KEY_PASSPHRASE = 'secret!'

DEFAULT_WAIT_TIME = 120  # 1 minute

TEMP_DIR = os.path.join('tests', 'temp')


@pytest.fixture(scope='module')
def key_pair_files():
    private_key = cli_util.generate_key()
    public_key = private_key.public_key()

    public_key_filename = os.path.join(TEMP_DIR, 'key_public.pem')
    private_key_filename = os.path.join(TEMP_DIR, 'key.pem')
    certificate_filename = os.path.join(TEMP_DIR, 'certificate.pem')

    with open(public_key_filename, "wb") as f:
        f.write(cli_util.serialize_key(public_key=public_key))

    with open(private_key_filename, "wb") as f:
        f.write(cli_util.serialize_key(private_key=private_key, passphrase=LB_PRIVATE_KEY_PASSPHRASE))

    # Various details about who we are. For a self-signed certificate the
    # subject and issuer are always the same.
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"WA"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"Seattle"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Oracle"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"company.com"),
    ])

    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        public_key
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        # Our certificate will be valid for 10 days
        datetime.datetime.utcnow() + datetime.timedelta(days=10)
    ).add_extension(
        x509.SubjectAlternativeName([x509.DNSName(u"localhost")]), critical=False).sign(private_key, hashes.SHA256(), default_backend())

    # Write our certificate out to disk.
    with open(certificate_filename, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))

    result = [public_key_filename, private_key_filename, certificate_filename]
    yield result

    for filename in result:
        if os.path.isfile(filename):
            os.remove(filename)


@pytest.fixture(scope='module')
def vcn_and_subnets(network_client):
    # create VCN
    vcn_name = util.random_name('cli_lb_test_vcn')
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
    subnet_name = util.random_name('cli_lb_test_subnet')
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
    subnet_name = util.random_name('cli_lb_test_subnet')
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

    yield [vcn_ocid, subnet_ocid_1, subnet_ocid_2]

    # delete VCN and subnets
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
def load_balancer(runner, config_file, config_profile, vcn_and_subnets):
    subnet_ocid_1 = vcn_and_subnets[1]
    subnet_ocid_2 = vcn_and_subnets[2]

    params = [
        'load-balancer', 'create',
        '-c', util.COMPARTMENT_ID,
        '--display-name', util.random_name('cli_lb'),
        '--shape-name', '100Mbps',
        '--subnet-ids', '["{}","{}"]'.format(subnet_ocid_1, subnet_ocid_2)
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # create lb returns work request
    response = json.loads(result.output)
    work_request_ocid = response['opc-work-request-id']

    get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=LB_PROVISIONING_TIME_SEC)
    util.validate_response(get_work_request_result)

    lb_ocid = json.loads(get_work_request_result.output)['data']['load-balancer-id']

    yield lb_ocid

    params = [
        'load-balancer', 'delete',
        '--load-balancer-id', lb_ocid,
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    util.wait_until(['lb', 'load-balancer', 'get', '--load-balancer-id', lb_ocid], 'TERMINATED', max_wait_seconds=LB_PROVISIONING_TIME_SEC, succeed_if_not_found=True)


@pytest.fixture(scope='module')
def backend_set(runner, config_file, config_profile, load_balancer):
    backend_set_name = util.random_name('cli_lb_backend_set')

    params = [
        'backend-set', 'create',
        '--name', backend_set_name,
        '--policy', 'ROUND_ROBIN',
        '--load-balancer-id', load_balancer,
        '--health-checker-protocol', 'HTTP',
        '--health-checker-return-code', '200',
        '--health-checker-url-path', '/healthcheck',
        '--health-checker-interval-in-ms', '60000',  # 1 minute
        '--session-persistence-cookie-name', '*',
        '--session-persistence-disable-fallback', 'false'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # create lb returns work request
    response = json.loads(result.output)
    work_request_ocid = response['opc-work-request-id']

    get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=DEFAULT_WAIT_TIME)
    util.validate_response(get_work_request_result)

    yield backend_set_name

    params = [
        'backend-set', 'delete',
        '--load-balancer-id', load_balancer,
        '--backend-set-name', backend_set_name,
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    response = json.loads(result.output)
    work_request_ocid = response['opc-work-request-id']

    get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=DEFAULT_WAIT_TIME)
    util.validate_response(get_work_request_result)


@pytest.fixture
def backend(runner, config_file, config_profile, load_balancer, backend_set):
    ip_address = '10.0.0.10'
    port = '80'
    params = [
        'backend', 'create',
        '--ip-address', ip_address,
        '--port', port,
        '--load-balancer-id', load_balancer,
        '--backend-set-name', backend_set,
        '--weight', '3'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # returns work request
    response = json.loads(result.output)
    work_request_ocid = response['opc-work-request-id']

    get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=DEFAULT_WAIT_TIME)
    util.validate_response(get_work_request_result)

    # backend name defaults to "ipaddress:port"
    backend_name = "{}:{}".format(ip_address, port)
    yield backend_name

    params = [
        'backend', 'delete',
        '--load-balancer-id', load_balancer,
        '--backend-set-name', backend_set,
        '--backend-name', backend_name,
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # returns work request
    response = json.loads(result.output)
    work_request_ocid = response['opc-work-request-id']

    get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=DEFAULT_WAIT_TIME)
    util.validate_response(get_work_request_result)


@pytest.fixture
def certificate(runner, config_file, config_profile, load_balancer, key_pair_files):
    private_key_filename = key_pair_files[1]
    certificate_filename = key_pair_files[2]

    cert_name = util.random_name('cli_lb_certificate')

    params = [
        'certificate', 'create',
        '--certificate-name', cert_name,
        '--load-balancer-id', load_balancer,
        '--ca-certificate-file', certificate_filename,
        '--private-key-file', private_key_filename,
        '--public-certificate-file', certificate_filename,
        '--passphrase', LB_PRIVATE_KEY_PASSPHRASE
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # returns work request
    response = json.loads(result.output)
    work_request_ocid = response['opc-work-request-id']

    get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=LB_PROVISIONING_TIME_SEC)
    util.validate_response(get_work_request_result)

    yield cert_name

    # delete cert
    params = [
        'certificate', 'delete',
        '--load-balancer-id', load_balancer,
        '--certificate-name', cert_name,
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    response = json.loads(result.output)
    work_request_ocid = response['opc-work-request-id']

    get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=LB_PROVISIONING_TIME_SEC)
    util.validate_response(get_work_request_result)


@util.slow
def test_load_balancer_operations(runner, config_file, config_profile, load_balancer):
    # list
    params = [
        'load-balancer', 'list',
        '-c', util.COMPARTMENT_ID
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    load_balancers = json.loads(result.output)['data']

    found_lb = False
    for lb in load_balancers:
        if lb['id'] == load_balancer:
            found_lb = True

    assert found_lb

    # update
    # params = [
    #     'load-balancer', 'update',
    #     '--load-balancer-id', load_balancer,
    #     '--display-name', util.random_name('cli_lb_updated')
    # ]

    # result = invoke(runner, config_file, config_profile, params)
    # util.validate_response(result)

    # # returns work request
    # response = json.loads(result.output)
    # work_request_ocid = response['opc-work-request-id']

    # get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=DEFAULT_WAIT_TIME)
    # util.validate_response(get_work_request_result)

    # get
    params = [
        'load-balancer', 'get',
        '--load-balancer-id', load_balancer
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # assert 'cli_lb_updated' in json.loads(result.output)['data']['display-name']


@util.slow
def test_certificate_operations(runner, config_file, config_profile, load_balancer, certificate):
    params = [
        'certificate', 'list',
        '--load-balancer-id', load_balancer
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    response = json.loads(result.output)
    found_cert = False
    for cert in response['data']:
        if cert['certificate-name'] == certificate:
            found_cert = True

    assert found_cert


@util.slow
def test_backend_set_operations(runner, config_file, config_profile, load_balancer, backend_set):
    # fixture handles create / delete
    params = [
        'backend-set', 'list',
        '--load-balancer-id', load_balancer
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    params = [
        'backend-set', 'get',
        '--load-balancer-id', load_balancer,
        '--backend-set-name', backend_set
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    params = [
        'backend-set', 'update',
        '--load-balancer-id', load_balancer,
        '--backend-set-name', backend_set,
        '--backends', '[]',
        '--policy', 'ROUND_ROBIN',
        '--health-checker-protocol', 'HTTP',
        '--health-checker-url-path', '/healthchecker',
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # returns work request
    response = json.loads(result.output)
    work_request_ocid = response['opc-work-request-id']

    get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=DEFAULT_WAIT_TIME)
    util.validate_response(get_work_request_result)


@util.slow
def test_backend_operations(runner, config_file, config_profile, load_balancer, backend_set, backend):
    # fixture handles create / delete
    params = [
        'backend', 'list',
        '--load-balancer-id', load_balancer,
        '--backend-set-name', backend_set
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    params = [
        'backend', 'update',
        '--load-balancer-id', load_balancer,
        '--backend-set-name', backend_set,
        '--backend-name', backend,
        '--weight', '2',
        '--offline', 'true',
        '--backup', 'false',
        '--drain', 'false'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # returns work request
    response = json.loads(result.output)
    work_request_ocid = response['opc-work-request-id']

    get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=DEFAULT_WAIT_TIME)
    util.validate_response(get_work_request_result)


@util.slow
def test_listener_operations(runner, config_file, config_profile, load_balancer, backend_set, certificate):
    # create listener
    listener_name = util.random_name('cli_listener')
    params = [
        'listener', 'create',
        '--default-backend-set-name', backend_set,
        '--load-balancer-id', load_balancer,
        '--name', listener_name,
        '--port', '8080',
        '--protocol', 'HTTP',
        '--ssl-certificate-name', certificate
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # returns a work request
    response = json.loads(result.output)
    work_request_ocid = response['opc-work-request-id']

    get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=LB_PROVISIONING_TIME_SEC)
    util.validate_response(get_work_request_result)

    # update listener
    params = [
        'listener', 'update',
        '--listener-name', listener_name,
        '--default-backend-set-name', backend_set,
        '--load-balancer-id', load_balancer,
        '--port', '8080',
        '--protocol', 'HTTP',
        '--ssl-certificate-name', certificate,
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # returns a work request
    response = json.loads(result.output)
    work_request_ocid = response['opc-work-request-id']

    get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=LB_PROVISIONING_TIME_SEC)
    util.validate_response(get_work_request_result)

    # delete listener
    params = [
        'listener', 'delete',
        '--load-balancer-id', load_balancer,
        '--listener-name', listener_name,
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # returns a work request
    response = json.loads(result.output)
    work_request_ocid = response['opc-work-request-id']

    get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=LB_PROVISIONING_TIME_SEC)
    util.validate_response(get_work_request_result)


@util.slow
def test_load_balancer_health_operations(runner, config_file, config_profile, load_balancer):
    params = [
        'load-balancer-health', 'get',
        '--load-balancer-id', load_balancer
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    params = [
        'load-balancer-health', 'list',
        '-c', util.COMPARTMENT_ID
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


@util.slow
def test_backend_set_health_operations(runner, config_file, config_profile, load_balancer, backend_set):
    params = [
        'backend-set-health', 'get',
        '--load-balancer-id', load_balancer,
        '--backend-set-name', backend_set
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


@util.slow
def test_backend_health_operations(runner, config_file, config_profile, load_balancer, backend_set, backend):
    params = [
        'backend-health', 'get',
        '--load-balancer-id', load_balancer,
        '--backend-set-name', backend_set,
        '--backend-name', backend
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


@util.slow
def test_health_checker_operations(runner, config_file, config_profile, load_balancer, backend_set):
    params = [
        'health-checker', 'update',
        '--load-balancer-id', load_balancer,
        '--backend-set-name', backend_set,
        '--interval-in-millis', '15000',
        '--port', '80',
        '--protocol', 'HTTP',
        '--response-body-regex', '.*',
        '--retries', '3',
        '--return-code', '200',
        '--timeout-in-millis', '1000',
        '--url-path', '/healthcheck'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # health-checker update returns work request
    response = json.loads(result.output)
    work_request_ocid = response['opc-work-request-id']

    get_work_request_result = util.wait_until(['lb', 'work-request', 'get', '--work-request-id', work_request_ocid], 'SUCCEEDED', max_wait_seconds=LB_PROVISIONING_TIME_SEC)
    util.validate_response(get_work_request_result)

    params = [
        'health-checker', 'get',
        '--load-balancer-id', load_balancer,
        '--backend-set-name', backend_set
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    assert 15000 == json.loads(result.output)['data']['interval-in-millis']


def test_list_lb_shapes(runner, config_file, config_profile):
    params = [
        'shape', 'list',
        '-c', util.COMPARTMENT_ID
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


def test_list_lb_protocols(runner, config_file, config_profile):
    params = [
        'protocol', 'list',
        '-c', util.COMPARTMENT_ID
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


def test_list_lb_policy(runner, config_file, config_profile):
    params = [
        'policy', 'list',
        '-c', util.COMPARTMENT_ID
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile', config_profile, 'lb'] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + ['--config-file', config_file, '--profile', config_profile, 'lb'] + params, ** args)

    return result
