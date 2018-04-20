# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from click.testing import CliRunner
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from oci_cli import cli_util
from . import tag_data_container
from . import test_config_container

import click
import datetime
import oci
import os
import os.path
import pytest
import random
import time


def pytest_addoption(parser):
    parser.addoption("--fast", action="store_true", default=False, help="Skip slow tests, as marked with the @slow annotation.")
    parser.addoption("--enable-long-running", action="store_true", default=False, help="Enables tests marked with the @enable_long_running annotation")
    parser.addoption("--config-profile", action="store", help="profile to use from the config file", default=oci.config.DEFAULT_PROFILE)
    parser.addoption("--vcr-record-mode", action="store", default='once', help="Record mode option for VCRpy library.")


def pytest_configure(config):
    test_config_container.vcr_mode = config.getoption("--vcr-record-mode")


@pytest.fixture(scope='session')
def malformed_config_file(config):
    # generate malformed config from real config
    sections = {
        'MISSING_USER': 'user',
        'MISSING_FINGERPRINT': 'fingerprint',
        'MISSING_KEY': 'key_file',
        'MISSING_TENANCY': 'tenancy',
        'MISSING_REGION': 'region'
    }

    malformed_config_file_path = os.path.join(get_resource_directory(), 'malformed_config')
    with open(malformed_config_file_path, 'w+') as f:
        for key in sections:
            f.write('\n\n')
            f.write('[{}]\n'.format(key))
            field_to_skip = sections[key]
            for valid_config_key in config:
                if valid_config_key != field_to_skip:
                    f.write('{} = {}\n'.format(valid_config_key, config[valid_config_key]))

        # write SPECIFY BAD ENDPOINT SECTION
        f.write('[SPECIFY_BAD_ENDPOINT]\n')
        for valid_config_key in config:
            f.write('{} = {}\n'.format(valid_config_key, config[valid_config_key]))
        f.write('endpoint = https://notaservice.us-phoenix-1.oraclecloud.com')

    yield malformed_config_file_path

    if os.path.exists(malformed_config_file_path):
        os.remove(malformed_config_file_path)


@pytest.fixture(scope='session')
def config_file():
    return os.environ['OCI_CLI_CONFIG_FILE']


@pytest.fixture(scope='session')
def config_profile(request):
    return request.config.getoption("--config-profile")


@pytest.fixture(scope='session')
def config(config_file, config_profile):
    config = oci.config.from_file(file_location=config_file, profile_name=config_profile)
    pass_phrase = os.environ.get('PYTHON_CLI_ADMIN_PASS_PHRASE')
    if pass_phrase:
        config['pass_phrase'] = pass_phrase
    return config


@pytest.fixture(scope="session")
def runner():
    # click does not distinguish between stdout and stderr in Result.output so we are wrapping invoke to strip out common stderr warnings
    # this allows the output to be json parseable which many tests expect
    cli_runner = CliRunner()
    old_invoke = cli_runner.invoke

    def invoke(*args, **kwargs):
        result = old_invoke(*args, **kwargs)
        if result.output and cli_util.LIST_NOT_ALL_ITEMS_RETURNED_WARNING in result.output:
            cleaned_output = result.output.replace(cli_util.LIST_NOT_ALL_ITEMS_RETURNED_WARNING, '')
            try:
                new_output_bytes = bytes(cleaned_output, result.runner.charset)
            except TypeError:
                new_output_bytes = cleaned_output
            finally:
                result = click.testing.Result(result.runner, new_output_bytes, result.exit_code, result.exception, result.exc_info)

        return result

    cli_runner.invoke = invoke
    return cli_runner


@pytest.fixture(scope='session')
def test_id():
    return str(random.randint(0, 1000000))


@pytest.fixture(scope='session')
def object_storage_client(config):
    return oci.object_storage.ObjectStorageClient(config)


@pytest.fixture(scope='session')
def network_client(config):
    return oci.core.VirtualNetworkClient(config)


@pytest.fixture(scope='session')
def compute_client(config):
    return oci.core.ComputeClient(config)


@pytest.fixture(scope='session')
def filestorage_client(config):
    return oci.file_storage.FileStorageClient(config)


@pytest.fixture(scope='session')
def identity_client(config):
    return oci.identity.IdentityClient(config)


@pytest.fixture(scope='session')
def dns_client(config):
    return oci.dns.DnsClient(config)


@pytest.fixture(scope='module')
def key_pair_files():
    temp_dir = os.path.join('tests', 'temp')
    private_key = cli_util.generate_key()
    public_key = private_key.public_key()

    public_key_filename = os.path.join(temp_dir, 'key_public.pem')
    private_key_filename = os.path.join(temp_dir, 'key.pem')
    certificate_filename = os.path.join(temp_dir, 'certificate.pem')

    with open(public_key_filename, "wb") as f:
        f.write(cli_util.serialize_key(public_key=public_key))

    with open(private_key_filename, "wb") as f:
        f.write(cli_util.serialize_key(private_key=private_key, passphrase='secret!'))

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
    from . import util

    with test_config_container.create_vcr().use_cassette('_conftest_fixture_vcn_and_subnets.yml'):
        # create VCN
        vcn_name = util.random_name('cli_lb_test_vcn')
        cidr_block = "10.0.0.0/16"
        vcn_dns_label = util.random_name('vcn', insert_underscore=False)

        create_vcn_details = oci.core.models.CreateVcnDetails()
        create_vcn_details.cidr_block = cidr_block
        create_vcn_details.display_name = vcn_name
        create_vcn_details.compartment_id = os.environ['OCI_CLI_COMPARTMENT_ID']
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
        create_subnet_details.compartment_id = os.environ['OCI_CLI_COMPARTMENT_ID']
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
        subnet_dns_label = util.random_name('subnet2', insert_underscore=False)

        create_subnet_details = oci.core.models.CreateSubnetDetails()
        create_subnet_details.compartment_id = os.environ['OCI_CLI_COMPARTMENT_ID']
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

    # For some reason VCR doesn't like that the post-yield stuff here is all in one cassette. Splitting into different cassettes seems to work
    with test_config_container.create_vcr().use_cassette('_conftest_fixture_vcn_and_subnets_delete.yml'):
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


@pytest.fixture(scope='session')
def tag_namespace_and_tags(identity_client, test_id):
    with test_config_container.create_vcr().use_cassette('_conftest_fixture_tag_namespace_and_tags.yml'):
        if not os.environ.get('OCI_CLI_TAG_NAMESPACE_ID'):
            tag_namespace_name = 'cli_tag_ns_{}'.format(test_id)
            create_tag_namespace_response = identity_client.create_tag_namespace(
                oci.identity.models.CreateTagNamespaceDetails(
                    compartment_id=os.environ['OCI_CLI_COMPARTMENT_ID'],
                    name=tag_namespace_name,
                    description='Python SDK integ test namespace'
                )
            )

            tag_namespace = create_tag_namespace_response.data
        else:
            print('Reusing tag namespace: {}'.format(os.environ.get('OCI_CLI_TAG_NAMESPACE_ID')))
            get_tag_namespace_response = identity_client.get_tag_namespace(os.environ.get('OCI_CLI_TAG_NAMESPACE_ID'))

            if get_tag_namespace_response.data.is_retired:
                update_tag_namespace_response = identity_client.update_tag_namespace(
                    get_tag_namespace_response.data.id,
                    oci.identity.models.UpdateTagNamespaceDetails(is_retired=False)
                )
                tag_namespace = update_tag_namespace_response.data
            else:
                tag_namespace = get_tag_namespace_response.data

        tags = []
        if not os.environ.get('OCI_CLI_TAG_ONE_NAME'):
            tag_one_name = 'cli_tag_{}'.format(test_id)
            create_tag_response = identity_client.create_tag(
                tag_namespace.id,
                oci.identity.models.CreateTagDetails(name=tag_one_name, description='CLI integration test tag')
            )
            tags.append(create_tag_response.data)
        else:
            print('Reusing tag: {}'.format(os.environ.get('OCI_CLI_TAG_ONE_NAME')))
            tags.append(get_and_reactivate_tag(identity_client, tag_namespace, os.environ.get('OCI_CLI_TAG_ONE_NAME')))

        if not os.environ.get('OCI_CLI_TAG_TWO_NAME'):
            tag_two_name = 'cli_tag2_{}'.format(test_id)
            create_tag_response = identity_client.create_tag(
                tag_namespace.id,
                oci.identity.models.CreateTagDetails(name=tag_two_name, description='CLI integration test tag')
            )
            tags.append(create_tag_response.data)
        else:
            print('Reusing tag: {}'.format(os.environ.get('OCI_CLI_TAG_TWO_NAME')))
            tags.append(get_and_reactivate_tag(identity_client, tag_namespace, os.environ.get('OCI_CLI_TAG_TWO_NAME')))

        # Avoid eventual consistency issue where we try and use tags we just created and get a 404 (though it
        # would succeed on retry)
        time.sleep(10)

        tag_data_container.tag_namespace = tag_namespace
        tag_data_container.tags = tags

    yield {'namespace': tag_namespace, 'tags': tags}

    with test_config_container.create_vcr().use_cassette('_conftest_fixture_tag_namespace_and_tags_retire.yml'):
        # Only retire if we're not reusing a namespace or tags, otherwise on parallel runs we can get conflicts since one run retires a tag that
        # another run expects to not be retired
        if not os.environ.get('OCI_CLI_TAG_NAMESPACE_ID') and not os.environ.get('OCI_CLI_TAG_ONE_NAME') and not os.environ.get('OCI_CLI_TAG_TWO_NAME'):
            for tag in tags:
                identity_client.update_tag(
                    tag.tag_namespace_id,
                    tag.name,
                    oci.identity.models.UpdateTagDetails(is_retired=True)
                )

            update_tag_namespace_response = identity_client.update_tag_namespace(
                tag_namespace.id,
                oci.identity.models.UpdateTagNamespaceDetails(is_retired=True)
            )


def get_and_reactivate_tag(identity_client, tag_namespace, tag_name):
    get_tag_response = identity_client.get_tag(
        tag_namespace.id,
        tag_name
    )

    if get_tag_response.data.is_retired:
        update_tag_response = identity_client.update_tag(
            tag_namespace.id,
            tag_name,
            oci.identity.models.UpdateTagDetails(is_retired=False)
        )

        return update_tag_response.data
    else:
        return get_tag_response.data


def get_resource_directory():
    """Get the absolute path to the test resources directory.
    File is located based on the relative location of this file (util.py).
    """
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, "resources")


def get_resource_path(file_name):
    return os.path.join(get_resource_directory(), file_name)
